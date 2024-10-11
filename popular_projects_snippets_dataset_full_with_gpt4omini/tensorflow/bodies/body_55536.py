# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_vgpu_test.py
super().setUp()
if self.already_run:
    raise RuntimeError(
        'Each test in this test suite must run in a separate process. '
        'Increase number of shards used to run this test.')
self.already_run = True
