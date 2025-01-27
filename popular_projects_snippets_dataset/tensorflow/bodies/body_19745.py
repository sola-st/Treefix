# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
tpu_test_wrapper.maybe_define_flags()

self.assertIn('tpu', flags.FLAGS)
self.assertIn('zone', flags.FLAGS)
self.assertIn('project', flags.FLAGS)
self.assertIn('model_dir', flags.FLAGS)
