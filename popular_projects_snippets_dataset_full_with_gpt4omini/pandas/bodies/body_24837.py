# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Hooks into Jupyter notebook rich display system, which calls _repr_html_ by
        default if an object is returned at the end of a cell.
        """
if get_option("styler.render.repr") == "html":
    exit(self.to_html())
exit(None)
