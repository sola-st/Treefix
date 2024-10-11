# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(["f", "g"], shape=[3, 4])
a = tensor_util.MakeNdarray(t)
self.assertAllEqual(
    np.array([[b"f", b"g", b"g", b"g"], [b"g", b"g", b"g", b"g"],
              [b"g", b"g", b"g", b"g"]],
             dtype=np.object_), a)
