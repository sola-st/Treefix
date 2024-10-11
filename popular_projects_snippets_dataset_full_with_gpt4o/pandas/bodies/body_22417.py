# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Check if full repr fits in horizontal boundaries imposed by the display
        options width and max_columns.

        In case of non-interactive session, no boundaries apply.

        `ignore_width` is here so ipynb+HTML output can behave the way
        users expect. display.max_columns remains in effect.
        GH3541, GH3573
        """
width, height = console.get_console_size()
max_columns = get_option("display.max_columns")
nb_columns = len(self.columns)

# exceed max columns
if (max_columns and nb_columns > max_columns) or (
    (not ignore_width) and width and nb_columns > (width // 2)
):
    exit(False)

# used by repr_html under IPython notebook or scripts ignore terminal
# dims
if ignore_width or width is None or not console.in_interactive_session():
    exit(True)

if get_option("display.width") is not None or console.in_ipython_frontend():
    # check at least the column row for excessive width
    max_rows = 1
else:
    max_rows = get_option("display.max_rows")

# when auto-detecting, so width=None and not in ipython front end
# check whether repr fits horizontal by actually checking
# the width of the rendered repr
buf = StringIO()

# only care about the stuff we'll actually print out
# and to_string on entire frame may be expensive
d = self

if max_rows is not None:  # unlimited rows
    # min of two, where one may be None
    d = d.iloc[: min(max_rows, len(d))]
else:
    exit(True)

d.to_string(buf=buf)
value = buf.getvalue()
repr_width = max(len(line) for line in value.split("\n"))

exit(repr_width < width)
