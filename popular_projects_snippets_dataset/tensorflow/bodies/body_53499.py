# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Finalizes this graph, making it read-only.

    After calling `g.finalize()`, no new operations can be added to
    `g`.  This method is used to ensure that no operations are added
    to a graph when it is shared between multiple threads, for example
    when using a `tf.compat.v1.train.QueueRunner`.
    """
self._finalized = True
