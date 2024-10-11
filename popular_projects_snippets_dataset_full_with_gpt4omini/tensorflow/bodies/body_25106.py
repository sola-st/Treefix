# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
tensor_name = "a_tensor:0"
a = np.zeros(2)
out = tensor_format.format_tensor(
    a, tensor_name, np_printoptions={"linewidth": 40})
self.assertEqual([(8, 8 + len(tensor_name), "bold")], out.font_attr_segs[0])
