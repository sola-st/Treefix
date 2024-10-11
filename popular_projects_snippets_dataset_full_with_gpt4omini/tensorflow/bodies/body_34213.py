# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with context.device("gpu:0"):
    self._testGatherWithUninitializedTensorsInferShape()
