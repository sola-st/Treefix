# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
if attr is None:
    self.skipTest('attr module is unavailable.')

@attr.s
class SampleAttr(object):
    field1 = attr.ib()
    field2 = attr.ib()

val1 = np.array([1.2, 3.4, 5.6])
val2 = np.array([[1, 2], [4, 3]])
val3 = np.array([10, 20, 30])

t1 = constant_op.constant(val1)
t2 = constant_op.constant(val2)

sample = SampleAttr(t1, t2)
with session.Session() as sess:
    result = sess.run(sample)
    self.assertIsInstance(result, SampleAttr)
    self.assertAllEqual(val1, result.field1)
    self.assertAllEqual(val2, result.field2)

    result = sess.run(sample, feed_dict={sample.field1: val3})
    self.assertIsInstance(result, SampleAttr)
    self.assertAllEqual(val3, result.field1)
    self.assertAllEqual(val2, result.field2)
