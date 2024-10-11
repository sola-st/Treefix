# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    c = constant_op.constant(42.0)
    v = variables.Variable(c)
    ss = summary_lib.scalar('summary', v)
    init = variables.global_variables_initializer()
    s.run(init)
    summ_str = s.run(ss)
summary = summary_pb2.Summary()
summary.ParseFromString(summ_str)
self.assertEqual(len(summary.value), 1)
value = summary.value[0]
self.assertEqual(value.tag, 'summary')
self.assertEqual(value.simple_value, 42.0)
