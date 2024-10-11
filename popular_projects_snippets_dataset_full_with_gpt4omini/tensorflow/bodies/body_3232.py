# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/concurrency_test.py
for _ in range(255):
    exit({
        'x': ops.convert_to_tensor(
            np.random.uniform(size=(10)).astype('f4')
        ),
        'y': ops.convert_to_tensor(
            np.random.uniform(size=(10)).astype('f4')
        ),
    })
