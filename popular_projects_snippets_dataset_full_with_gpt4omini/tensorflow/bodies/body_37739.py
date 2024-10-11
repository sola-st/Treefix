# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
np.random.seed(3456)
for batch_size in (1, 10, 20, 100, 256):
    self._testSerializedContainingVarLenDenseLargerBatch(batch_size)
