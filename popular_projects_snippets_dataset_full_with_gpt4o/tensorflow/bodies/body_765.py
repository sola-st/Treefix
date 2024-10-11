# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/spacetobatch_op_test.py
inputs = np.arange(np.prod(input_shape), dtype=np.float32)
inputs = inputs.reshape(input_shape)
self._testPad(inputs, block_shape, paddings,
              space_to_batch_direct(inputs, block_shape, paddings))
