# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
self.assertEqual(options.threading, options.experimental_threading)
options.threading.max_intra_op_parallelism = 20
options.experimental_threading.max_intra_op_parallelism = 40
pb = options._to_proto()
result = options_lib.Options()
result._from_proto(pb)
self.assertEqual(result.experimental_threading.max_intra_op_parallelism,
                 result.threading.max_intra_op_parallelism)
