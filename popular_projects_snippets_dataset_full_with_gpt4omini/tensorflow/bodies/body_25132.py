# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array([], dtype=np.float32)
out = tensor_format.numeric_summary(x)
self.assertEqual(["No numeric summary available due to empty tensor."],
                 out.lines)
