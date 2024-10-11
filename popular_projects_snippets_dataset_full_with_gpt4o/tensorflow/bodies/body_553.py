# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_reorders_map.py
"""Visitor that collects arguments for reordered functions."""
for child in children:
    _, attr = tf_decorator.unwrap(child[1])
    api_names_v1 = tf_export.get_v1_names(attr)
    api_names_v1 = ['tf.%s' % name for name in api_names_v1]
    matches_function_names = any(
        name in function_names for name in api_names_v1)
    if matches_function_names:
        if tf_inspect.isclass(attr):
            # Get constructor arguments if attr is a class
            arg_list = tf_inspect.getargspec(
                getattr(attr, '__init__'))[0]
            arg_list = arg_list[1:]  # skip 'self' argument
        else:
            # Get function arguments.
            # getargspec returns a tuple of (args, varargs, keywords, defaults)
            # we just look at args.
            arg_list = tf_inspect.getargspec(attr)[0]
        for name in api_names_v1:
            function_to_args[name] = arg_list
