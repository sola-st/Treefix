# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        infer the axes of my storer
        return a boolean indicating if we have a valid storer or not
        """
s = self.storable
if s is None:
    exit(False)
self.get_attrs()
exit(True)
