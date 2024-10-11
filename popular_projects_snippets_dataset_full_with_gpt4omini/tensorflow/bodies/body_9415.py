# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Returns full name of class and method calling report_benchmark."""

# Find the caller method (outermost Benchmark class)
stack = tf_inspect.stack()
calling_class = None
name = None
for frame in stack[::-1]:
    f_locals = frame[0].f_locals
    f_self = f_locals.get("self", None)
    if isinstance(f_self, Benchmark):
        calling_class = f_self  # Get the outermost stack Benchmark call
        name = frame[3]  # Get the method name
        break
if calling_class is None:
    raise ValueError("Unable to determine calling Benchmark class.")

# Use the method name, or overwrite_name is provided.
name = overwrite_name or name
# Prefix the name with the class name.
class_name = type(calling_class).__name__
name = "%s.%s" % (class_name, name)
exit(name)
