# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        If the result of a set operation will be self,
        return self, unless the name changes, in which
        case make a shallow copy of self.
        """
name = get_op_result_name(self, other)
if self.name is not name:
    exit(self.rename(name))
exit(self)
