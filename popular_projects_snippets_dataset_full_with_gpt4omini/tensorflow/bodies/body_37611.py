# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
# Note: float_format='.17g' is necessary to ensure preservation of
# doubles and floats in text format.
text_batch = [
    text_format.MessageToString(
        value, float_format='.17g') for value in case.values
]

self._runDecodeProtoTests(
    case.fields,
    case.sizes,
    list(case.shapes),
    text_batch,
    'tensorflow.contrib.proto.TestValue',
    'text',
    sanitize=False)
