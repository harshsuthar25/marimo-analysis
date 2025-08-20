# 24f2000011@ds.study.iitm.ac.in  (email as a comment)

import marimo as mo
app = mo.App()

# Cell 0: imports (downstream cells depend on np, plt, mo)
@app.cell
def __():
    import numpy as np
    import matplotlib.pyplot as plt
    import marimo as mo
    return np, plt, mo

# Cell 1: UI source (downstream cells depend on n.value)
@app.cell
def __(mo):
    # Interactive slider widget controlling dataset size
    n = mo.ui.slider(10, 300, value=100, label="Number of points")
    # Lightweight helper text near the control
    mo.md(f"Use the slider to change data size → **n = {n.value}**")
    return n,

# Cell 2: Data (depends on n.value from Cell 1)
@app.cell
def __(np, n):
    # Generate data based on the UI state
    x = np.linspace(0, 10, n.value)
    y = np.sin(x) + 0.1 * np.random.randn(n.value)
    # x,y are consumed by the plotting cell
    return x, y

# Cell 3: Plot (depends on x, y, and n) and expose a UI element
@app.cell
def __(plt, x, y, n, mo):
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"sin(x)+noise  ·  n={n.value}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    # Expose as a UI component so it can be embedded elsewhere
    plot = mo.ui.matplotlib(fig)
    return plot,

# Cell 4: Dynamic Markdown (depends on n and plot)
@app.cell
def __(mo, n, plot):
    # Dynamic, self-documenting cell that updates with the widget
    bullets = "🟢" * max(1, n.value // 25)  # visual indicator of n
    mo.md(f"""
### Interactive Relationship Demo (Marimo)
- Points selected: **{n.value}** {bullets}  
- Cells are reactive: changing the slider updates data ➜ plot ➜ this text.

{plot}
""")

if __name__ == "__main__":
    app.run()
