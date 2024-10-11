# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
# Now try with the packed serialization.
# We test the packed representations by loading the same test cases using
# PackedTestValue instead of TestValue. To do this we rely on the text
# format being the same for packed and unpacked fields, and reparse the test
# message using the packed version of the proto.
in_bufs = [
    # Note: float_format='.17g' is necessary to ensure preservation of
    # doubles and floats in text format.
    text_format.Parse(
        text_format.MessageToString(
            value, float_format='.17g'),
        test_example_pb2.PackedTestValue()).SerializeToString()
    for value in case.values
]

# np.array silently truncates strings if you don't specify dtype=object.
in_bufs = np.reshape(np.array(in_bufs, dtype=object), list(case.shapes))
exit(self._testRoundtrip(
    in_bufs, 'tensorflow.contrib.proto.PackedTestValue', case.fields))
