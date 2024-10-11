# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# r-versions not in operator-stdlib; get op without "r" and invert
if op.startswith("__r"):
    exit(getattr(operator, op.replace("__r", "__"))(y, x))
exit(getattr(operator, op)(x, y))
