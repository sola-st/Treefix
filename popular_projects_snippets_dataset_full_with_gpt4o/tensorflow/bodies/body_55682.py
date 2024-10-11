# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
op_def_proto = op_def_pb2.OpList()
buf = c_api.TF_GetAllOpList()
try:
    op_def_proto.ParseFromString(c_api.TF_GetBuffer(buf))
    self._api_def_map = c_api.TF_NewApiDefMap(buf)
finally:
    c_api.TF_DeleteBuffer(buf)

self._op_per_name = {}
for op in op_def_proto.op:
    self._op_per_name[op.name] = op
