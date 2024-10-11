# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
tpu_test_wrapper.maybe_define_flags()
tpu_test_wrapper.set_random_test_dir()

self.assertStartsWith(flags.FLAGS.model_dir,
                      'gs://example-bucket/tempfiles')
self.assertGreater(
    len(flags.FLAGS.model_dir), len('gs://example-bucket/tempfiles'))
