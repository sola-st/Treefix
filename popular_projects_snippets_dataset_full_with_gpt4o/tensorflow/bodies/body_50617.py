# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    i = constant_op.constant(7)
    with ops.name_scope('outer'):
        im1 = summary_lib.scalar('inner', i, family='family')
        self.assertEqual(im1.op.name, 'outer/family/inner')
        im2 = summary_lib.scalar('inner', i, family='family')
        self.assertEqual(im2.op.name, 'outer/family/inner_1')
    sm1, sm2 = s.run([im1, im2])
summary = summary_pb2.Summary()

summary.ParseFromString(sm1)
values = summary.value
self.assertEqual(len(values), 1)
self.assertEqual(values[0].tag, 'family/outer/family/inner')
self.assertEqual(values[0].simple_value, 7.0)

summary.ParseFromString(sm2)
values = summary.value
self.assertEqual(len(values), 1)
self.assertEqual(values[0].tag, 'family/outer/family/inner_1')
self.assertEqual(values[0].simple_value, 7.0)
