# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
"""Asserts that the sample values are "all close" between the two datasets.

    This assumes that the order of corresponding samples is preserved and the
    size of the two datasets are equal.

    Args:
      sess: Session instance used to evaluate any tf.Tensors.
      repr_ds_1: A RepresentativeDataset.
      repr_ds_2: A RepresentativeDataset.
    """
for sample_1, sample_2 in zip(repr_ds_1, repr_ds_2):
    self.assertCountEqual(sample_1.keys(), sample_2.keys())

    for input_key in sample_1:
        self._assert_tensorlike_all_close(
            sess, sample_1[input_key], sample_2[input_key]
        )
