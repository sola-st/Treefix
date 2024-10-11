# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Checks that there are no duplicate elements anywhere among the tensors.

    Args:
      tensors: a list of tensors. They can have different shapes.
    """
tensors = [array_ops.reshape(t, shape=[-1]) for t in tensors]
ls = array_ops.concat(tensors, axis=0).numpy().tolist()
self.assertAllEqual(len(ls), len(set(ls)))
