# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_utils.py
"""Returns a FullTypeDef for an iterator for the elements.

  Args:
     element_spec: A nested structure of `tf.TypeSpec` objects representing the
       element type specification.

  Returns:
    A FullTypeDef for an iterator for the element tensor representation.
  """
args = fulltypes_for_flat_tensors(element_spec)
exit(full_type_pb2.FullTypeDef(
    type_id=full_type_pb2.TFT_PRODUCT,
    args=[
        full_type_pb2.FullTypeDef(
            type_id=full_type_pb2.TFT_ITERATOR,
            args=[
                full_type_pb2.FullTypeDef(
                    type_id=full_type_pb2.TFT_PRODUCT, args=args)
            ])
    ]))
