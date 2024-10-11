# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta0 = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=2, infer_shape=False)
ta1 = tensor_array_ops.TensorArray(
    dtype=dtypes.int32, size=4, infer_shape=True)

ta0 = ta0.write(0, 0.)
ta1 = ta1.write(0, 1)

with ops.control_dependencies([v0.assign_add(1.0)]):
    ta0 = ta0.identity()

with ops.control_dependencies([v1.assign_add(1.0)]):
    ta1 = ta1.identity()

read0 = ta0.read(0)
read1 = ta1.read(0)

size0 = ta0.size()
size1 = ta1.size()

tensor_arrays[0] = ta0
tensor_arrays[1] = ta1

exit([read0, read1, size0, size1, v0, v1])
