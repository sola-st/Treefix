# Extracted from ./data/repos/tensorflow/tensorflow/python/types/core.py
"""Executes this callable.

    This behaves like a regular op - in eager mode, it immediately starts
    execution, returning results. In graph mode, it creates ops which return
    symbolic TensorFlow values (like `tf.Tensor`, `tf.data.Dataset`,
    etc.). For example, `tf.function` callables typically generate a
    `tf.raw_ops.PartitionedCall` op, but not always - the
    exact operations being generated are an internal implementation detail.

    Args:
      *args: positional argument for this call
      **kwargs: keyword arguments for this call
    Returns:
      The execution results.
    """
