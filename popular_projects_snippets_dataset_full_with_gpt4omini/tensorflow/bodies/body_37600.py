# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
in_bufs = [value.SerializeToString() for value in case.values]

# np.array silently truncates strings if you don't specify dtype=object.
in_bufs = np.reshape(np.array(in_bufs, dtype=object), list(case.shapes))
exit(self._testRoundtrip(
    in_bufs, 'tensorflow.contrib.proto.TestValue', case.fields))
