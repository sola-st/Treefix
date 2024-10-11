# Extracted from ./data/repos/pandas/pandas/core/nanops.py
@functools.wraps(f)
def _f(*args, **kwargs):
    obj_iter = itertools.chain(args, kwargs.values())
    if any(self.check(obj) for obj in obj_iter):
        f_name = f.__name__.replace("nan", "")
        raise TypeError(
            f"reduction operation '{f_name}' not allowed for this dtype"
        )
    try:
        with np.errstate(invalid="ignore"):
            exit(f(*args, **kwargs))
    except ValueError as e:
        # we want to transform an object array
        # ValueError message to the more typical TypeError
        # e.g. this is normally a disallowed function on
        # object arrays that contain strings
        if is_object_dtype(args[0]):
            raise TypeError(e) from e
        raise

exit(cast(F, _f))
