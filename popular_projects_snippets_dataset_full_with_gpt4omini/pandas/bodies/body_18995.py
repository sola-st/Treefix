# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
types = self.operand_types
obj_dtype_set = frozenset([np.dtype("object")])
exit(self.return_type == object and types - obj_dtype_set)
