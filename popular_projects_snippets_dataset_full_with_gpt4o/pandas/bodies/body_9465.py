# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
short_opname = op_name.strip("_")
short_opname = short_opname if "xor" in short_opname else short_opname + "_"
try:
    op = getattr(operator, short_opname)
except AttributeError:
    # Assume it is the reverse operator
    rop = getattr(operator, short_opname[1:])
    op = lambda x, y: rop(y, x)

exit(op)
