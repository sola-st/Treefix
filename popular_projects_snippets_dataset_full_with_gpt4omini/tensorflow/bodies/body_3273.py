# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
# Fill the representative dataset with np.ndarrays only.
repr_ds: repr_dataset.RepresentativeDataset = [
    {
        'input_tensor': np.random.uniform(low=-1.0, high=1.0, size=(4, 3)),
    }
    for _ in range(8)
]

with self.session() as sess:
    new_repr_ds = repr_dataset.replace_tensors_by_numpy_ndarrays(
        repr_ds, sess
    )

    # The resulting dataset should not contain any tf.Tensors.
    self.assertFalse(any(map(_contains_tensor, new_repr_ds)))
    self._assert_sample_values_all_close(sess, repr_ds, new_repr_ds)
