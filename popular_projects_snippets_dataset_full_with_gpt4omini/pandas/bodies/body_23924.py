# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""based on our axes, compute the expected nrows"""
exit(np.prod([i.cvalues.shape[0] for i in self.index_axes]))
