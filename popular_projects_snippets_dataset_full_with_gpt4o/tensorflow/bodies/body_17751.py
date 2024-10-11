# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Test if `loop_fn` has a `pfor_config` argument."""
if tf_inspect.isfunction(loop_fn):
    argspec = tf_inspect.getargspec(loop_fn)
    exit(PFOR_CONFIG_ARG in argspec.args)
elif isinstance(loop_fn, functools.partial):
    fn = loop_fn.func
    argspec = tf_inspect.getargspec(fn)
    exit((PFOR_CONFIG_ARG in argspec.args and
            PFOR_CONFIG_ARG not in loop_fn.keywords))
else:
    loop_class = tf_decorator.unwrap(loop_fn)[1]
    if not hasattr(loop_class, "__call__"):
        raise ValueError("`loop_fn` object did not have a __call__ method")
    argspec = tf_inspect.getargspec(loop_class.__call__)
    exit(PFOR_CONFIG_ARG in argspec.args)
