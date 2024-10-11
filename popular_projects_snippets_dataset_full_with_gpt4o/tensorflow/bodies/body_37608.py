# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
batch = [value.SerializeToString() for value in case.values]
self._runDecodeProtoTests(
    case.fields,
    case.sizes,
    list(case.shapes),
    batch,
    'tensorflow.contrib.proto.TestValue',
    'binary',
    sanitize=False)
