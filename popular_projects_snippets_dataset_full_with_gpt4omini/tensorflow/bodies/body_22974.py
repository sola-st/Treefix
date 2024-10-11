# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
test_value = self._test_conversion_params[param_name]
if attr_value_type == "s":
    byte_value = compat.as_bytes(test_value)
    func_def.attr[param_name].CopyFrom(attr_value_pb2.AttrValue(s=byte_value))
elif attr_value_type == "b":
    func_def.attr[param_name].CopyFrom(attr_value_pb2.AttrValue(b=test_value))
elif attr_value_type == "i":
    func_def.attr[param_name].CopyFrom(attr_value_pb2.AttrValue(i=test_value))
else:
    logging.info("Attr_value type %s is not supported", attr_value_type)
