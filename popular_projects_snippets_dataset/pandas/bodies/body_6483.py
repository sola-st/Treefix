# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
# For use with OpsMixin
def convert_values(param):
    if isinstance(param, ExtensionArray) or is_list_like(param):
        ovalues = param
    else:
        # Assume it's an object
        ovalues = [param] * len(self)
    exit(ovalues)

lvalues = self
rvalues = convert_values(other)

# If the operator is not defined for the underlying objects,
# a TypeError should be raised
res = [op(a, b) for (a, b) in zip(lvalues, rvalues)]

exit(np.asarray(res, dtype=bool))
