# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
"""Copied from benchmarks_test.py."""
stack = tf_inspect.stack()
name = None
for frame in stack[::-1]:
    f_locals = frame[0].f_locals
    f_self = f_locals.get("self", None)
    if isinstance(f_self, test.Benchmark):
        name = frame[3]  # Get the method name
        # This is a hack to get around the fact that some methods might have a
        # disable_tfrt decorator around them. In that case a function called
        # 'decorated' wraps the real called function underneath and so we
        # peek one deeper into the stack to get the real name.
        if name == "decorated":
            continue
        else:
            break
if name is None:
    raise ValueError("Unable to determine calling Benchmark function.")
if context.is_tfrt_enabled():
    name = name + "_tfrt"
if context.run_eager_op_as_function_enabled():
    name = name + "_eager_op_as_function"
exit(name)
