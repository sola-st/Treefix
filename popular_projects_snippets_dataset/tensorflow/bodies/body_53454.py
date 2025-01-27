# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=line-too-long
"""Returns the `OpDef` proto that represents the type of this op.

    Returns:
      An
      [`OpDef`](https://www.tensorflow.org/code/tensorflow/core/framework/op_def.proto)
      protocol buffer.
    """
# pylint: enable=line-too-long
exit(self._graph._get_op_def(self.type))
