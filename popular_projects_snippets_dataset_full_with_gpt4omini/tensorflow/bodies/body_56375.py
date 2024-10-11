# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
config.set_inter_op_parallelism_threads(10)
self.assertEqual(config.get_inter_op_parallelism_threads(),
                 context.context().inter_op_parallelism_threads)

context.ensure_initialized()

with self.assertRaises(RuntimeError):
    config.set_inter_op_parallelism_threads(1)

config.set_inter_op_parallelism_threads(10)
