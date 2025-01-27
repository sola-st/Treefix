# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
# Reset ta because we're going to change the shape, else shape
# inference will throw an error.
ta = tensor_array_ops.TensorArray(
    dtype=tf_dtype, tensor_array_name="foo", size=3)

# Try unpacking an empty matrix, which should not cause an error.
w2 = ta.unstack(convert([[], [], []]))
r0 = w2.read(0)
r1 = w2.read(1)
r2 = w2.read(2)
exit([r0, r1, r2])
