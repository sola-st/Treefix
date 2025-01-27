# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
exit(string_ops.reduce_join(
    string_ops.reduce_join(
        ops.convert_to_tensor(sorted(kwargs.items())),
        axis=1,
        separator='='),
    axis=0,
    separator=', '))
