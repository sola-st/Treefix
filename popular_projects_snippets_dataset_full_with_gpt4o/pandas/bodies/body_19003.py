# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
super().__init__(op, (lhs, rhs))
self.lhs = lhs
self.rhs = rhs

self._disallow_scalar_only_bool_ops()

self.convert_values()

try:
    self.func = _binary_ops_dict[op]
except KeyError as err:
    # has to be made a list for python3
    keys = list(_binary_ops_dict.keys())
    raise ValueError(
        f"Invalid binary operator {repr(op)}, valid operators are {keys}"
    ) from err
