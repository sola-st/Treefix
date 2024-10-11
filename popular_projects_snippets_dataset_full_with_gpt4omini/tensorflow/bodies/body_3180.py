# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
for _ in range(8):
    exit({
        'input_tensor': ops.convert_to_tensor(
            np.random.uniform(low=0, high=150, size=(1, 3, 4, 3)).astype(
                'f4'
            )
        ),
    })
