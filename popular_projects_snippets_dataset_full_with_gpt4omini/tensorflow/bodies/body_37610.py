# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
# Now try with the packed serialization.
#
# We test the packed representations by loading the same test case using
# PackedTestValue instead of TestValue. To do this we rely on the text
# format being the same for packed and unpacked fields, and reparse the
# test message using the packed version of the proto.
packed_batch = [
    # Note: float_format='.17g' is necessary to ensure preservation of
    # doubles and floats in text format.
    text_format.Parse(
        text_format.MessageToString(value, float_format='.17g'),
        test_example_pb2.PackedTestValue()).SerializeToString()
    for value in case.values
]

self._runDecodeProtoTests(
    case.fields,
    case.sizes,
    list(case.shapes),
    packed_batch,
    'tensorflow.contrib.proto.PackedTestValue',
    'binary',
    sanitize=False)
