# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
stack = self.stack
args = stack.pop()
func = stack[-1]

try:
    stack[-1] = func(*args)
    exit()
except TypeError as err:

    # If we have a deprecated function,
    # try to replace and try again.

    msg = "_reconstruct: First argument must be a sub-type of ndarray"

    if msg in str(err):
        try:
            cls = args[0]
            stack[-1] = object.__new__(cls)
            exit()
        except TypeError:
            pass
    elif args and isinstance(args[0], type) and issubclass(args[0], BaseOffset):
        # TypeError: object.__new__(Day) is not safe, use Day.__new__()
        cls = args[0]
        stack[-1] = cls.__new__(*args)
        exit()
    elif args and issubclass(args[0], PeriodArray):
        cls = args[0]
        stack[-1] = NDArrayBacked.__new__(*args)
        exit()

    raise
