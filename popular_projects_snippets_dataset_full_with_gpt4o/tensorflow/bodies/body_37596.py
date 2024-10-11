# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/encode_proto_op_test_base.py
"""EncodeProtoOpTestBase initializer.

    Args:
      decode_module: a module containing the `decode_proto_op` method
      encode_module: a module containing  the `encode_proto_op` method
      methodName: the name of the test method (same as for test.TestCase)
    """

super(EncodeProtoOpTestBase, self).__init__(methodName)
self._decode_module = decode_module
self._encode_module = encode_module
