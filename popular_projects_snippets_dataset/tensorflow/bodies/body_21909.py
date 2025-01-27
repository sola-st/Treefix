# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.assertRaisesRegex(
    ValueError, "must have the same keys"):
    inp.batch_join(
        [{
            "c": 12,
            "s": 123,
            "S": "a"
        }, {
            "cool": -12,
            "s": 99,
            "S": "b"
        }],
        batch_size=8)
