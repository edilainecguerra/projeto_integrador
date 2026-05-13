from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils.translation import gettext_lazy as _
from datetime import date, timedelta

def home_view(request):
    """Display the home page with process steps and completed tasks."""
    completed_count = 0
    completed_percentage = 0
    completed_tasks = []
    upcoming_tasks = []
    total_tasks = 0
    weekly_progress = []
    selected_week = request.GET.get('week', 'this')
    if selected_week not in ['this', 'last']:
        selected_week = 'this'

    if request.user.is_authenticated:
        task_qs = Task.objects.filter(user=request.user)
        total_tasks = task_qs.count()
        completed_count = task_qs.filter(completed=True).count()
        completed_tasks = task_qs.filter(completed=True).order_by('-due_date')[:5]
        upcoming_tasks = task_qs.filter(completed=False).order_by('due_date')[:3]
        completed_percentage = round((completed_count / total_tasks) * 100) if total_tasks else 0

        today = date.today()
        week_offset_days = 7 if selected_week == 'last' else 0
        week_start = (today - timedelta(days=today.weekday())) - timedelta(days=week_offset_days)
        week_days = [week_start + timedelta(days=i) for i in range(7)]
        counts = [task_qs.filter(completed=True, due_date=day).count() for day in week_days]
        max_count = max(counts) if counts else 1
        if max_count == 0:
            max_count = 1

        weekly_progress = []
        for day, count in zip(week_days, counts):
            ratio = (count / max_count) if max_count else 0
            if count == 0:
                level = _('No progress')
                color = 'slate'
            elif ratio < 0.34:
                level = _('Light progress')
                color = 'sky'
            elif ratio < 0.67:
                level = _('Steady progress')
                color = 'blue'
            else:
                level = _('Strong progress')
                color = 'emerald'

            weekly_progress.append({
                'label': day.strftime('%a').upper(),
                'count': count,
                'height': int(ratio * 100) if max_count else 10,
                'size': 60 + int(ratio * 36),
                'level': level,
                'color': color,
                'date': day,
                'is_today': day == today,
            })

    return render(request, 'home.html', {
        'completed_count': completed_count,
        'completed_percentage': completed_percentage,
        'completed_tasks': completed_tasks,
        'upcoming_tasks': upcoming_tasks,
        'total_tasks': total_tasks,
        'weekly_progress': weekly_progress,
        'selected_week': selected_week,
        'today': date.today(),
    })

@login_required
def task_list(request):
    """Display list of tasks for authenticated user."""
    status = request.GET.get('status', 'all')
    priority = request.GET.get('priority', 'all')
    search = request.GET.get('search', '').strip()

    tasks = Task.objects.filter(user=request.user)

    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    if priority in ['H', 'M', 'L']:
        tasks = tasks.filter(priority=priority)

    if search:
        tasks = tasks.filter(title__icontains=search) | tasks.filter(description__icontains=search)

    tasks = tasks.order_by('completed', 'due_date')

    return render(request, 'list.html', {
        'tasks': tasks,
        'status': status,
        'priority': priority,
        'search': search,
        'today': date.today(),
    })

@login_required
def focus_timer(request):
    """Render user-facing focus timer view."""
    return render(request, 'focus_timer.html')

@login_required
def new_task(request):
    """Create a new task."""
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description', '').strip()
        priority = request.POST.get('priority', 'M')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority or 'M'
        )
        return redirect('/tasks/')
    return render(request, 'new.html')

@login_required
def complete_task(request, id):
    """Mark task as completed."""
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('/tasks/')

@login_required
def delete_task(request, id):
    """Delete a task."""
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('/tasks/')

from django.contrib.auth import authenticate, login

def login_view(request):
    """Authenticate user login."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    """Logout user."""
    logout(request)
    return redirect('/login/')
