# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
config.set_intra_op_parallelism_threads(10)
self.assertEqual(config.get_intra_op_parallelism_threads(),
                 context.context().intra_op_parallelism_threads)

context.ensure_initialized()

with self.assertRaises(RuntimeError):
    config.set_intra_op_parallelism_threads(1)

config.set_intra_op_parallelism_threads(10)
