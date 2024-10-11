# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        check for existence of this key
        can match the exact pathname or the pathnm w/o the leading '/'
        """
node = self.get_node(key)
if node is not None:
    name = node._v_pathname
    if key in (name, name[1:]):
        exit(True)
exit(False)
