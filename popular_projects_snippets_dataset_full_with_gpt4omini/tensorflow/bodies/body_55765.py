# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
num_iters = 100
duration = self._computeMnistMlpGrads(
    unified_math_ops,
    unified_nn_ops,
    tape_lib,
    True,
    num_iters,
    hidden_layers=10,
    hidden_size=100,
    batch_size=1)
self.report_benchmark(
    name="TenHiddenLayerMnistEagerUnified",
    iters=num_iters,
    wall_time=duration)
