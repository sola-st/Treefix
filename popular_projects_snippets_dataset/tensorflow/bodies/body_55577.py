# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_util_test.py
with self.assertRaisesRegex(TypeError, "Failed to convert value"):
    _op_def_util.ConvertPyObjectToAttributeType(value, attr_type)
