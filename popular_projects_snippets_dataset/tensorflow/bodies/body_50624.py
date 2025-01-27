# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    i = array_ops.ones((5, 3, 4))
    with ops.name_scope('outer'):
        aud = summary_lib.audio('inner', i, 0.2, max_outputs=3)
    summary_str = s.run(aud)
summary = summary_pb2.Summary()
summary.ParseFromString(summary_str)
values = summary.value
self.assertEqual(len(values), 3)
tags = sorted(v.tag for v in values)
expected = sorted('outer/inner/audio/{}'.format(i) for i in range(3))
self.assertEqual(tags, expected)
