# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
node.attr[key].CopyFrom(
    attr_value_pb2.AttrValue(tensor=tensor_util.make_tensor_proto(
        value, dtype=dtype, shape=shape)))
