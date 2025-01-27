# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding.py
"""Applies this Sharding attribute to `operation`.

    Args:
      operation: A tf.Operation to add sharding annotation.
    """
attr_value = attr_value_pb2.AttrValue(s=self._proto.SerializeToString())
# pylint: disable=protected-access
operation._set_attr('_XlaSharding', attr_value)
