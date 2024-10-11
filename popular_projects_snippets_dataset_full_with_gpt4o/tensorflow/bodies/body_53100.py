# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
exit(while_v2.while_loop(
    lambda v: v < 4.,
    lambda v: v * v, [x],
    return_same_structure=False,
    name="while_1"))  # x**2
