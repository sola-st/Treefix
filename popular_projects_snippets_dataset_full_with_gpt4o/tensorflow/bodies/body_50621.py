# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    i = array_ops.ones((5, 4, 4, 3))
    with ops.name_scope('outer'):
        summ_op = summary_lib.histogram('inner', i)
    summary_str = s.run(summ_op)
summary = summary_pb2.Summary()
summary.ParseFromString(summary_str)
self.assertEqual(len(summary.value), 1)
self.assertEqual(summary.value[0].tag, 'outer/inner')
