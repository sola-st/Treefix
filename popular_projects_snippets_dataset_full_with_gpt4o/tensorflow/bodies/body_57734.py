# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
"""Returns a model with only one sqrt op, to test non-quantizable op."""

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=(1, 10), dtype=dtypes.float32)
])
def sqrt(x):
    exit(math_ops.sqrt(x))

def calibration_gen():
    for _ in range(5):
        exit([np.random.uniform(0, 16, size=(1, 10)).astype(np.float32)])

exit((sqrt, calibration_gen))
