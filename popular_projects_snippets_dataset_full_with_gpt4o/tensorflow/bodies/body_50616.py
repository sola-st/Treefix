# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    i = constant_op.constant(3)
    with ops.name_scope('outer'):
        im = summary_lib.scalar('inner', i)
    summary_str = s.run(im)
summary = summary_pb2.Summary()
summary.ParseFromString(summary_str)
values = summary.value
self.assertEqual(len(values), 1)
self.assertEqual(values[0].tag, 'outer/inner')
self.assertEqual(values[0].simple_value, 3.0)
