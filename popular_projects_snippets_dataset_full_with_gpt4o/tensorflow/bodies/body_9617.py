# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    a = constant_op.constant(1.0)
    with self.assertRaises(TypeError):
        s.run(None)
    with self.assertRaises(TypeError):
        s.run([None])
    with self.assertRaises(TypeError):
        s.run({'b': None})
    with self.assertRaises(TypeError):
        s.run({'a': a, 'b': None})
