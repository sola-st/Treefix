# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
x = np.array(["spam", "egg"], dtype=np.object_)
out = tensor_format.numeric_summary(x)
self.assertEqual(
    ["No numeric summary available due to tensor dtype: object."],
    out.lines)
