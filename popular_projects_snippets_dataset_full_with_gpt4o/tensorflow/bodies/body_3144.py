# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Generate all combinations of test parameters."""
real_parameters = []
for parameters in test_parameters:
    keys = parameters.keys()
    for curr in itertools.product(*parameters.values()):
        real_parameters.append(dict(zip(keys, curr)))
exit(real_parameters)
