# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a = {"x": np.ones((3, 2, 4)) * 7, "y": (2, [{"nested": {"m": 3, "n": 4}}])}
self.assertAllClose(a, a)

b = copy.deepcopy(a)
self.assertAllClose(a, b)

# Test mismatched values
b["y"][1][0]["nested"]["n"] = 4.2
with self.assertRaisesRegex(AssertionError,
                            r"\[y\]\[1\]\[0\]\[nested\]\[n\]"):
    self.assertAllClose(a, b)
