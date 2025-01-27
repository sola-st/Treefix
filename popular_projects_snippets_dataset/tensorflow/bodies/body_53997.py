# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a = 7
b = (2., 3.)
c = np.ones((3, 2, 4)) * 7.
expected = {"a": a, "b": b, "c": c}

# Identity.
self.assertAllClose(expected, expected)
self.assertAllClose(expected, dict(expected))

# With each item removed.
for k in expected:
    actual = dict(expected)
    del actual[k]
    with self.assertRaisesRegex(AssertionError, r"mismatched keys"):
        self.assertAllClose(expected, actual)

    # With each item changed.
with self.assertRaisesRegex(AssertionError, r"Not equal to tolerance"):
    self.assertAllClose(expected, {"a": a + 1e-5, "b": b, "c": c})
with self.assertRaisesRegex(AssertionError, r"Shape mismatch"):
    self.assertAllClose(expected, {"a": a, "b": b + (4.,), "c": c})
c_copy = np.array(c)
c_copy[1, 1, 1] += 1e-5
with self.assertRaisesRegex(AssertionError, r"Not equal to tolerance"):
    self.assertAllClose(expected, {"a": a, "b": b, "c": c_copy})
