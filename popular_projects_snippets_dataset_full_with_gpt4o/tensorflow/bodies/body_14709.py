# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
tensors = [ops.convert_to_tensor(0.1), ops.convert_to_tensor(0.2)]

flattened = nest.flatten(tensors, expand_composites=True)
# Each ndarray contains only one tensor, so the flattened output should be
# just 2 tensors in a list.
self.assertLen(flattened, 2)
self.assertIsInstance(flattened[0], ops.Tensor)
self.assertIsInstance(flattened[1], ops.Tensor)

repacked = nest.pack_sequence_as(tensors, flattened, expand_composites=True)
self.assertLen(repacked, 2)
self.assertIsInstance(repacked[0], np_arrays.ndarray)
self.assertIsInstance(repacked[1], np_arrays.ndarray)

self.assertAllClose(tensors, repacked)
