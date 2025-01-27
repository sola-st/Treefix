# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
ret_types = set()
for t in f_types:

    if isinstance(t, Callable):
        # Note: these are undocummented - may be version-specific!
        # Callable[[x], y]: __args__ are (x, y)
        args = t.__args__
        if args:
            ret_types.add(args[-1])
        else:
            ret_types.add(Any)
    else:
        raise NotImplementedError('callable type {}'.format(type(t)))

    # Side effects can not be inferred based on type alone.
side_effects = None
exit((ret_types, side_effects))
