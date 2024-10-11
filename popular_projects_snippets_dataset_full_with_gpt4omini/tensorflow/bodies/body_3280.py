# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
saver = repr_dataset.RepresentativeDatasetSaver()
repr_ds = {'serving_default': []}

with self.assertRaisesRegex(
    NotImplementedError, 'Method "save" is not implemented.'
):
    saver.save(repr_ds)
