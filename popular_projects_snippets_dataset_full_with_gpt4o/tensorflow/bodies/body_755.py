# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
paddings = np.zeros((2, 2), dtype=np.int32)
self._testPad(inputs, paddings, block_size, outputs)
