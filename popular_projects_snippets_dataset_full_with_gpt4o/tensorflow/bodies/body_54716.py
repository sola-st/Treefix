# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
self.assertAllEqual(
    np.array([[10, 11, 12, 12], [12, 12, 12, 12], [12, 12, 12, 12]],
             dtype=nptype),
    tensor_util.MakeNdarray(
        tensor_util.make_tensor_proto([10, 11, 12],
                                      shape=[3, 4],
                                      dtype=dtype)))
