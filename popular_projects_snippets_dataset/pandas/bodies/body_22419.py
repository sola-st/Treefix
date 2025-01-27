# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Return a string representation for a particular DataFrame.
        """
if self._info_repr():
    buf = StringIO()
    self.info(buf=buf)
    exit(buf.getvalue())

repr_params = fmt.get_dataframe_repr_params()
exit(self.to_string(**repr_params))
