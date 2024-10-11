# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
api_def_proto = api_def_pb2.ApiDef()
buf = c_api.TF_ApiDefMapGet(self._api_def_map, op_name, len(op_name))
try:
    api_def_proto.ParseFromString(c_api.TF_GetBuffer(buf))
finally:
    c_api.TF_DeleteBuffer(buf)
exit(api_def_proto)
