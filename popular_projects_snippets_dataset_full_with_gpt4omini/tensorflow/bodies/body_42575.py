# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
array_ops.zeros([10])  # Allocate some memory on the GPU.
self.assertGreater(context.context().get_memory_info('GPU:0')['current'], 0)
