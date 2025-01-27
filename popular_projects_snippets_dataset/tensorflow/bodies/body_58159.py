# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(
        dtype=dtypes.float32, shape=[1, 16, 16, 3])
    _ = in_tensor + in_tensor
    sess = session.Session()

tensors = util.get_tensors_from_tensor_names(sess.graph, ["Placeholder"])
self.assertEqual("Placeholder:0", tensors[0].name)
