# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
self._benchmarkUniform(
    'uniform_f16', dtype=dtypes.float16, use_xla_jit=True)
