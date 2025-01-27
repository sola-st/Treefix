# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/signature/signature_def_utils.py
signature_def = meta_graph_pb2.SignatureDef()
signature_def.ParseFromString(serialized)
exit(signature_def)
