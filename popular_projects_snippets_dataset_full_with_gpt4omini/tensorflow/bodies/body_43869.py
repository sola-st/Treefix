# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/basic_list_test.py
self.all_inputs_tensors = True
self.assertFunctionMatchesEager(element_access)
self.assertFunctionMatchesEager(element_update)

# TODO(mdan): This should raise a compilation, not runtime, error.
with self.assertRaisesRegex(
    ValueError,
    'cannot stack a list without knowing its element type; '
    'use set_element_type to annotate it'):
    self.function(type_not_annotated)(3)

self.assertFunctionMatchesEager(simple_fill, 5)
self.assertFunctionMatchesEager(nested_fill, 5, 3)
self.assertFunctionMatchesEager(read_write_loop, 4)
self.assertFunctionMatchesEager(simple_empty, 0)
self.assertFunctionMatchesEager(simple_empty, 2)
self.assertFunctionMatchesEager(simple_empty, 4)

# TODO(mdan): Allow explicitly setting the element shape to mitigate these.
# TODO(mdan): This should raise a friendlier runtime error.
# The error should spell out that empty lists cannot be stacked.
# Alternatively, we can also insert conditionals that construct a zero-sized
# Tensor of the appropriate type and shape, but we first want to make sure
# that doesn't degrade performance.
with self.assertRaises(ValueError):
    self.function(simple_fill)(0)
with self.assertRaises(ValueError):
    self.function(nested_fill)(0, 3)
