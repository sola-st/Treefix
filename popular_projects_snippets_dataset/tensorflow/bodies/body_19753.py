# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
tpu_test_wrapper.maybe_define_flags()
tpu_test_wrapper.set_random_test_dir()
first = flags.FLAGS.model_dir
tpu_test_wrapper.set_random_test_dir()
second = flags.FLAGS.model_dir

self.assertNotEqual(first, second)
