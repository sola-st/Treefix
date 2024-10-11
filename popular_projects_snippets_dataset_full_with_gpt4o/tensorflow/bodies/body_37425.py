# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
meta = config_pb2.RunMetadata()

with ops.name_scope('foo', skip_on_eager=False):
    event = self.run_metadata(name='my_name', data=meta, step=1)
    first_val = event.summary.value[0]

self.assertEqual('foo/my_name', first_val.tag)
