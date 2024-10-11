# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
if attr is None:
    self.skipTest('attr module is unavailable.')

@attr.s
class SampleAttr(object):
    field0 = attr.ib()
    field1 = attr.ib()

v1 = 10
v2 = 20
v3 = np.float32(1.2)
v4 = np.float32(3.4)
v5 = np.float64(100.001)
v6 = np.float64(-23.451)
arr1 = np.array([1.2, 6.7, 3.4])
arr2 = np.array([7, 11, 3])
sample = SampleAttr(
    SampleAttr(
        SampleAttr(constant_op.constant(v1), constant_op.constant(v2)),
        SampleAttr(constant_op.constant(arr1), constant_op.constant(arr2))),
    {'A': SampleAttr(constant_op.constant(v3), constant_op.constant(v4)),
     'B': [SampleAttr(constant_op.constant(v5), constant_op.constant(v6))]})

with session.Session() as sess:
    result = sess.run(sample)
    self.assertIsInstance(result, SampleAttr)
    self.assertIsInstance(result.field0, SampleAttr)
    self.assertIsInstance(result.field0.field0, SampleAttr)
    self.assertIsInstance(result.field0.field1, SampleAttr)
    self.assertIsInstance(result.field0.field1.field0, np.ndarray)
    self.assertAllEqual(arr1, result.field0.field1.field0)
    self.assertIsInstance(result.field0.field1.field1, np.ndarray)
    self.assertAllEqual(arr2, result.field0.field1.field1)
    self.assertIsInstance(result.field1, dict)
    self.assertIn('A', result.field1)
    self.assertIn('B', result.field1)
    self.assertIsInstance(result.field1['A'], SampleAttr)
    self.assertAllEqual(
        [v3, v4],
        [result.field1['A'].field0, result.field1['A'].field1])
    self.assertIsInstance(result.field1['B'], list)
    self.assertEqual(1, len(result.field1['B']))
    self.assertIsInstance(result.field1['B'][0], SampleAttr)
    self.assertAllEqual(
        [v5, v6],
        [result.field1['B'][0].field0, result.field1['B'][0].field1])
