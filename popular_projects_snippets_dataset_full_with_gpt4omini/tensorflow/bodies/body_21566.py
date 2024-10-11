# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with self.assertRaisesRegex(errors.NotFoundError,
                            "Unsuccessful TensorSliceReader"):
    py_checkpoint_reader.NewCheckpointReader("non-existent")
