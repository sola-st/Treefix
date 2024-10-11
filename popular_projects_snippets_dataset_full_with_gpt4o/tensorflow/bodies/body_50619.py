# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
with self.cached_session() as s:
    i = array_ops.ones((5, 4, 4, 3))
    with ops.name_scope('outer'):
        im = summary_lib.image('inner', i, max_outputs=3)
    summary_str = s.run(im)
summary = summary_pb2.Summary()
summary.ParseFromString(summary_str)
values = summary.value
self.assertEqual(len(values), 3)
tags = sorted(v.tag for v in values)
expected = sorted('outer/inner/image/{}'.format(i) for i in range(3))
self.assertEqual(tags, expected)
