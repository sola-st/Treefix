# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Returns a LaTeX representation for a particular object.
        Mainly for use with nbconvert (jupyter notebook conversion to pdf).
        """
if config.get_option("styler.render.repr") == "latex":
    exit(self.to_latex())
else:
    exit(None)
