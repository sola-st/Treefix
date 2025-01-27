# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
result = function_pb2.FunctionDef()
result.CopyFrom(f_def)
result.attr.pop("_construction_context", None)
exit(result)
