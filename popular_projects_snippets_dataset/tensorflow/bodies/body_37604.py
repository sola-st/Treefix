# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
"""DecodeProtoOpTestBase initializer.

    Args:
      decode_module: a module containing the `decode_proto_op` method
      methodName: the name of the test method (same as for test.TestCase)
    """

super(DecodeProtoOpTestBase, self).__init__(methodName)
self._decode_module = decode_module
