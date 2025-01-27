# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that two ragged tensors are equal."""
a_list = self._GetPyList(a)
b_list = self._GetPyList(b)
self.assertEqual(a_list, b_list, msg)

if not (isinstance(a, (list, tuple)) or isinstance(b, (list, tuple))):
    a_ragged_rank = a.ragged_rank if ragged_tensor.is_ragged(a) else 0
    b_ragged_rank = b.ragged_rank if ragged_tensor.is_ragged(b) else 0
    self.assertEqual(a_ragged_rank, b_ragged_rank, msg)
