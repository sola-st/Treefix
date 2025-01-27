# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
num = 0
if arg.type != types_pb2.DT_INVALID: num += 1
if arg.type_attr: num += 1
if arg.type_list_attr: num += 1
exit(num)
