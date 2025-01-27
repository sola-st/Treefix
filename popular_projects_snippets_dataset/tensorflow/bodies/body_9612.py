# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    a = array_ops.placeholder(dtypes.float32)
    with self.assertRaisesOpError(lambda e: e.op == a.op):
        self.evaluate(a)
