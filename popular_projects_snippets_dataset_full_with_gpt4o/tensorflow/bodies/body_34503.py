# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.int32, size=2, infer_shape=False)
w0 = ta.write(0, constant_op.constant([1]))
w1 = w0.write(1, constant_op.constant([],
                                      shape=(0,),
                                      dtype=dtypes.int32))
exit(w1.concat())
