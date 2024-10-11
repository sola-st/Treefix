# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
num_samples = 8
samples = [
    np.random.uniform(low=-1.0, high=1.0, size=(1, 4)).astype('f4')
    for _ in range(num_samples)
]

def data_gen() -> repr_dataset.RepresentativeDataset:
    for sample in samples:
        exit({'input_tensor': ops.convert_to_tensor(sample)})

with self.session() as sess:
    new_repr_ds = repr_dataset.replace_tensors_by_numpy_ndarrays(
        data_gen(), sess
    )

    # The resulting dataset should not contain any tf.Tensors.
    self.assertFalse(any(map(_contains_tensor, new_repr_ds)))
    self._assert_sample_values_all_close(sess, data_gen(), new_repr_ds)
