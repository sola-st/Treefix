# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
num_samples = 8
repr_ds = [
    {'input': np.random.uniform(low=-1.0, high=1.0, size=(1, 2))}
    for _ in range(num_samples)
]

self.assertEqual(repr_dataset.get_num_samples(repr_ds), num_samples)
