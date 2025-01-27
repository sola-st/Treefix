# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
loader = repr_dataset.RepresentativeDatasetLoader()

with self.assertRaisesRegex(
    NotImplementedError, 'Method "load" is not implemented.'
):
    loader.load()
