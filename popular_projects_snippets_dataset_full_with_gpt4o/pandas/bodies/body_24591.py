# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Convert elements in ``crow`` to bold."""
exit([
    f"\\textbf{{{x}}}" if j < ilevels and x.strip() not in ["", "{}"] else x
    for j, x in enumerate(crow)
])
