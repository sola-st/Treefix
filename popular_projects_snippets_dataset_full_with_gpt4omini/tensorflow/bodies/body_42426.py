# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(errors.NotFoundError):
    execute(b'BlahBlahBlah', num_outputs=1, inputs=[], attrs=None)
