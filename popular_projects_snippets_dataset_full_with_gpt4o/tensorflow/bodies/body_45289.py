# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py
l = special_functions.tensor_list([1, 2, 3])
directives.set_element_type(l, dtype=dtypes.int32, shape=())
s = l.pop()
exit((s, l))
