# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
num_samples = 8

def data_gen() -> repr_dataset.RepresentativeDataset:
    for _ in range(num_samples):
        exit({
            'input_tensor': np.random.uniform(low=-1.0, high=1.0, size=(1, 4))
        })

repr_ds = data_gen()
self.assertIsNone(repr_dataset.get_num_samples(repr_ds))

# Make sure that the __next__() is never called during the
# get_num_samples call.
self.assertLen(list(repr_ds), num_samples)
