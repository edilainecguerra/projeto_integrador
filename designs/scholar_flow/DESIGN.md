# Design System Specification: The Academic Curator

## 1. Overview & Creative North Star
This design system moves away from the "industrial utility" of typical productivity tools and toward a philosophy we call **"The Academic Curator."** 

The goal is to transform the student's chaotic schedule into a serene, editorial experience. We achieve this by rejecting rigid, boxed-in grids in favor of **Tonal Layering** and **Intentional Asymmetry**. By utilizing high-contrast typography scales and "breathing" white space, we create an environment that feels less like a spreadsheet and more like a high-end digital journal. The interface should feel like a series of physical layers—stacked sheets of frosted glass and premium paper—that guide the eye through focus-oriented greens and trustworthy blues without the friction of traditional borders.

---

## 2. Colors & Surface Philosophy
We utilize a sophisticated palette of deep navy and vibrant emerald, balanced by a neutral hierarchy of "cool" surfaces.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections. Layout boundaries must be established exclusively through background color shifts. For example, a `surface-container-low` component should sit on a `surface` background to define its edges.

### Surface Hierarchy & Nesting
Instead of a flat grid, use the surface tiers to create "nested" depth:
*   **Background (`#f8f9fa`):** The primary canvas.
*   **Surface-Container-Lowest (`#ffffff`):** Reserved for the most important interactive elements (e.g., the active Task Card).
*   **Surface-Container-High (`#e7e8e9`):** Used for persistent secondary UI like the Sidebar or Calendar gutters.

### The "Glass & Gradient" Rule
To elevate the "Modern" requirement, floating elements (like Tooltips or Quick-Add Modals) must use **Glassmorphism**. 
*   **Style:** Apply `surface` at 70% opacity with a `20px` backdrop-blur. 
*   **Signature Textures:** For main CTAs or "Focus Mode" headers, use a subtle linear gradient from `primary` (#00478d) to `primary-container` (#005eb8) at a 135-degree angle to provide a sense of "soul" and depth.

---

## 3. Typography: Editorial Authority
We pair the structural precision of **Inter** with the geometric character of **Manrope** to create a hierarchy that feels both professional and accessible.

*   **Display (Manrope):** Used for high-level motivation (e.g., "Good Morning, Alex"). Use `display-lg` (3.5rem) to create a bold, editorial focal point.
*   **Headlines (Manrope):** `headline-md` (1.75rem) serves as the anchor for major sections like "Today’s Lectures" or "Weekly Progress."
*   **Body (Inter):** `body-lg` (1rem) is the workhorse. It must be set with generous line-height (1.6) to ensure long reading sessions don't cause eye strain.
*   **Labels (Inter):** `label-md` (0.75rem) in `on-surface-variant` color is used for metadata, ensuring a clear distinction between content and "UI noise."

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often a crutch for poor layout. In this system, depth is achieved through the **Layering Principle.**

*   **Tonal Stacking:** Place a `surface-container-lowest` card on a `surface-container-low` section. This creates a soft, natural "lift" that mimics physical paper without the clutter of drop shadows.
*   **Ambient Shadows:** If an element must float (e.g., a dragged task), use an extra-diffused shadow: `box-shadow: 0 12px 32px rgba(25, 28, 29, 0.06);`. The shadow color is a tinted version of `on-surface`, never pure black.
*   **The "Ghost Border" Fallback:** If a border is required for accessibility, use the `outline-variant` token at **15% opacity**. 100% opaque borders are strictly forbidden.

---

## 5. Components: Intentional Primitives

### Task Cards & Lists
*   **The Rule:** No divider lines between items.
*   **Execution:** Use `8px` (Spacing 2) of vertical white space to separate list items. For cards, use a `surface-container-low` background on a `surface` canvas.
*   **Status Indicators:** Use `secondary` (#1b6d24) for completed tasks and `tertiary` (#5000d2) for high-priority academic deadlines.

### Progress Bars
*   **Style:** Roundedness `full` (9999px).
*   **Track:** Use `surface-container-highest`.
*   **Indicator:** A gradient from `secondary` to `secondary-fixed-dim` to represent "growth" and "focus."

### Sidebar Navigation
*   **Surface:** `surface-container-low`.
*   **Active State:** Instead of a highlight box, use a vertical "pill" indicator in `primary` on the far left and shift the typography to `title-md` weight.

### Calendar Widgets
*   **Grid:** Avoid internal grid lines. Use a `surface-container-lowest` background for the current day and `surface-dim` for "out of month" dates. 
*   **Events:** Use `primary-fixed` for general routines and `secondary-fixed` for deep-work sessions.

### Input Fields
*   **Style:** Minimalist. No bottom border or full box. Use a `surface-container-highest` background with a `md` (0.75rem) corner radius.
*   **Focus State:** A 2px `surface-tint` glow with 10% opacity—no harsh outlines.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical layouts. A sidebar that is significantly wider than usual can feel like a "workspace" rather than just a menu.
*   **Do** leverage `tertiary` (#5000d2) for "uniquely student" moments like Exam Countdowns or GPA tracking to provide a visual "pop."
*   **Do** prioritize white space. If a screen feels "busy," increase the spacing between containers rather than adding more borders.

### Don't:
*   **Don't** use pure black (#000000) for text. Always use `on-surface` (#191c1d) to maintain the premium, soft-ink look.
*   **Don't** use standard "Success Green." Use the specified `secondary` (#1b6d24) which is a more sophisticated, forest-leaning "Focus Green."
*   **Don't** use sharp corners. Everything must adhere to the **Roundedness Scale**, specifically `md` (0.75rem) for cards and `lg` (1rem) for major containers.