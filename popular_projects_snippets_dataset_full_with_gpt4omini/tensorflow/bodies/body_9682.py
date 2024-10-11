# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    c = constant_op.constant(42.0, name='c')
    d = constant_op.constant(43.0, name=u'd')
    e = constant_op.constant(44.0, name=b'e')
    f = constant_op.constant(45.0, name=r'f')

    self.assertIsInstance(c.name, six.text_type)
    self.assertIsInstance(d.name, six.text_type)
    self.assertIsInstance(e.name, six.text_type)
    self.assertIsInstance(f.name, six.text_type)

    self.assertEqual(42.0, sess.run('c:0'))
    self.assertEqual(42.0, sess.run(u'c:0'))
    self.assertEqual(42.0, sess.run(b'c:0'))
    self.assertEqual(42.0, sess.run(r'c:0'))

    self.assertEqual(43.0, sess.run('d:0'))
    self.assertEqual(43.0, sess.run(u'd:0'))
    self.assertEqual(43.0, sess.run(b'd:0'))
    self.assertEqual(43.0, sess.run(r'd:0'))

    self.assertEqual(44.0, sess.run('e:0'))
    self.assertEqual(44.0, sess.run(u'e:0'))
    self.assertEqual(44.0, sess.run(b'e:0'))
    self.assertEqual(44.0, sess.run(r'e:0'))

    self.assertEqual(45.0, sess.run('f:0'))
    self.assertEqual(45.0, sess.run(u'f:0'))
    self.assertEqual(45.0, sess.run(b'f:0'))
    self.assertEqual(45.0, sess.run(r'f:0'))
