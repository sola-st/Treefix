# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
"""Checks that there are no duplicate elements anywhere among the tensors.

    Args:
      tensors: a list of tensors. They can have different shapes.
    """
values = [array_ops.reshape(t, shape=[-1]) for t in tensors]
values = array_ops.concat(values, axis=0)
values = self.evaluate(values)
values = values.tolist()
self.assertAllEqual(len(values), len(set(values)))
