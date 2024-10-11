# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Sets the corresponding node's `experimental_type` field.

    See the description of `NodeDef.experimental_type` for more info.

    Args:
      type_proto: A FullTypeDef proto message. The root type_if of this object
        must be `TFT_PRODUCT`, even for ops which only have a singlre return
        value.
    """
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    if (type_proto.type_id
        not in (full_type_pb2.TFT_UNSET, full_type_pb2.TFT_PRODUCT)):
        raise ValueError("error setting the type of ", self.name,
                         ": expected TFT_UNSET or TFT_PRODUCT, got ",
                         type_proto.type_id)
    pywrap_tf_session.SetFullType(c_graph, self._c_op,
                                  type_proto.SerializeToString())  # pylint:disable=protected-access
