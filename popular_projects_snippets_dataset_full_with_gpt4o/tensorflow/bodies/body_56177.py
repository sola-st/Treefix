# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_utils.py
"""Convert a list of FullType Def into a single FullType Def."""
exit(full_type_pb2.FullTypeDef(
    type_id=full_type_pb2.TFT_PRODUCT, args=fulltype_list))
