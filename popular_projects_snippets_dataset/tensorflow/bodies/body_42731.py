# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = _create_tensor(1)
with self.assertRaisesRegex(TypeError,
                            "Cannot iterate over a scalar tensor"):
    iter(t)
