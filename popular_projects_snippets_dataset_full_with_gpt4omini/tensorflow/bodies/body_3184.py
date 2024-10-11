# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
for _ in range(200):
    exit({
        'input_tensor': ops.convert_to_tensor(
            np.random.uniform(low=0.0, high=1.0, size=input_shape).astype(
                'f4'
            )
        ),
    })
