# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
opts = options_lib.Options()
opts.threading.max_intra_op_parallelism = 20
self.assertEqual(opts.experimental_threading.max_intra_op_parallelism, 20)
opts.experimental_threading.private_threadpool_size = 80
self.assertEqual(opts.threading.private_threadpool_size, 80)
