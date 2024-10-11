# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(dtype=dtypes.float32, shape=[4])
    out_tensors = array_ops.split(
        value=in_tensor, num_or_size_splits=[1, 1, 1, 1], axis=0)

expect_names = ["split", "split:1", "split:2", "split:3"]
for i in range(len(expect_names)):
    got_name = util.get_tensor_name(out_tensors[i])
    self.assertEqual(got_name, expect_names[i])
