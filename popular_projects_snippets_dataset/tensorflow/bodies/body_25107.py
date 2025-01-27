# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
tensor_name = "a_tensor:0"
debug_op = "DebugIdentity"
a = np.zeros(2)
out = tensor_format.format_tensor(
    a, "%s:%s" % (tensor_name, debug_op), np_printoptions={"linewidth": 40})
self.assertEqual([(8, 8 + len(tensor_name), "bold"),
                  (8 + len(tensor_name) + 1,
                   8 + len(tensor_name) + 1 + len(debug_op), "yellow")],
                 out.font_attr_segs[0])
