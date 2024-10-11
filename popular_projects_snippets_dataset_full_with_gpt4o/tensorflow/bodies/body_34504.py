# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.int32, size=3, infer_shape=False)
w0 = ta.write(0, constant_op.constant([8]))
w1 = w0.write(1, constant_op.constant([],
                                      shape=(0,),
                                      dtype=dtypes.int32))
w2 = w1.write(2, constant_op.constant([9]))
exit(w2.concat())
