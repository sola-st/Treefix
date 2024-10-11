# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    input_tensor = array_ops.placeholder(dtypes.float32, None)
    with self.assertRaisesRegex(ValueError, "fully defined shape"):
        _ = inp.input_producer(input_tensor)
