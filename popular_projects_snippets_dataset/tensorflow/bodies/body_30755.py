# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
x1 = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
x2 = [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
inp_tensors = [constant_op.constant(x1, shape=(2, 3), dtype=dtypes.float32),
               constant_op.constant(x2, shape=(2, 3), dtype=dtypes.float32)]

# Test concat gradient with axis == -2
self._testGradientsForAxis(inp_tensors, -2, output_shape=[4, 3])

# Test concat gradient with unknown-shape tensors.
x1_placeholder = array_ops.placeholder(dtypes.float32)
x2_placeholder = array_ops.placeholder(dtypes.float32)
inp_tensors_placeholders = [x1_placeholder, x2_placeholder]
feed_dict = {x1_placeholder: x1, x2_placeholder: x2}
self._testGradientsForAxis(
    inp_tensors_placeholders, -1, output_shape=[2, 6], feed_dict=feed_dict)

# Test IndexedSlices concat gradient.
self._testIndexedSlicesGradientsForAxis(
    inp_tensors, -2, output_shape=[2, 3], gather_indexes=[2, 0])

# We don't support calculating IndexedSlices concat gradient for
# negative indexes when rank is not known.
with self.assertRaises(ValueError):
    self._testIndexedSlicesGradientsForAxis(
        inp_tensors_placeholders, -2, output_shape=[2, 3],
        gather_indexes=[2, 0], feed_dict=feed_dict)
