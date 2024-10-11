# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_util_test.py
proto = attr_value_pb2.AttrValue()
text_format.Parse(pbtxt, proto)
result = _op_def_util.SerializedAttrValueToPyObject(
    proto.SerializeToString())

self.assertEqual(expected, result)
