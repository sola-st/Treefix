# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
num_tensors = 4
samples = [
    np.random.uniform(low=-1.0, high=1.0, size=(3, 3)).astype('f4')
    for _ in range(num_tensors)
]

repr_ds: repr_dataset.RepresentativeDataset = [
    {
        'tensor_key': ops.convert_to_tensor(sample),
    }
    for sample in samples
]

# Extend the representative dataset with np.ndarrays.
repr_ds.extend(
    [
        {'tensor_key': np.random.uniform(low=-1.0, high=1.0, size=(3, 3))}
        for _ in range(4)
    ]
)

random.shuffle(repr_ds)

with self.session() as sess:
    new_repr_ds = repr_dataset.replace_tensors_by_numpy_ndarrays(
        repr_ds, sess
    )

    # The resulting dataset should not contain any tf.Tensors.
    self.assertFalse(any(map(_contains_tensor, new_repr_ds)))
    self._assert_sample_values_all_close(sess, repr_ds, new_repr_ds)
