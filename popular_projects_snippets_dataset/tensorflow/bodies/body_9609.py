# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session(
    config=config_pb2.ConfigProto(use_per_session_threads=True)):
    inp = constant_op.constant(10.0, name='W1')
    self.assertAllEqual(inp, 10.0)
