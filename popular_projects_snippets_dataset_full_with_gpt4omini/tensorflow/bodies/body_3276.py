# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset_test.py
for _ in range(num_samples):
    exit({
        'input_tensor': np.random.uniform(low=-1.0, high=1.0, size=(1, 4))
    })
