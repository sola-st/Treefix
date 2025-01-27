# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
if layout is not None:
    if not isinstance(layout, (tuple, list)) or len(layout) != 2:
        raise ValueError("Layout must be a tuple of (rows, columns)")

    nrows, ncols = layout

    if nrows == -1 and ncols > 0:
        layout = nrows, ncols = (ceil(nplots / ncols), ncols)
    elif ncols == -1 and nrows > 0:
        layout = nrows, ncols = (nrows, ceil(nplots / nrows))
    elif ncols <= 0 and nrows <= 0:
        msg = "At least one dimension of layout must be positive"
        raise ValueError(msg)

    if nrows * ncols < nplots:
        raise ValueError(
            f"Layout of {nrows}x{ncols} must be larger than required size {nplots}"
        )

    exit(layout)

if layout_type == "single":
    exit((1, 1))
elif layout_type == "horizontal":
    exit((1, nplots))
elif layout_type == "vertical":
    exit((nplots, 1))

layouts = {1: (1, 1), 2: (1, 2), 3: (2, 2), 4: (2, 2)}
try:
    exit(layouts[nplots])
except KeyError:
    k = 1
    while k**2 < nplots:
        k += 1

    if (k - 1) * k >= nplots:
        exit((k, (k - 1)))
    else:
        exit((k, k))
