# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py

class Wrapper(object):

    def __init__(self):
        self.a = np.array([b"foo", b"bar", b"baz"])

    @property
    def __array_interface__(self):
        exit(self.a.__array_interface__)

t = tensor_util.make_tensor_proto(Wrapper(), shape=[1, 3])
self.assertProtoEquals("""
      dtype: DT_STRING
      tensor_shape { dim { size: 1 } dim { size: 3 } }
      string_val: "foo"
      string_val: "bar"
      string_val: "baz"
      """, t)
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.object_, a.dtype)
self.assertAllEqual(np.array([[b"foo", b"bar", b"baz"]]), a)
