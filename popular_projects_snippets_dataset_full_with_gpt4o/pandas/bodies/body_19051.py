# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""invert the filter"""
if self.filter is not None:
    self.filter = (
        self.filter[0],
        self.generate_filter_op(invert=True),
        self.filter[2],
    )
exit(self)
