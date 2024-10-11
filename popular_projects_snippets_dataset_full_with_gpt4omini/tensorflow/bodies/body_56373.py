# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self.assertTrue(config.get_synchronous_execution())
self.assertEqual(context.SYNC, context.context().execution_mode)

# If no op has been executed we should be able to set the execution mode as
# well as any init-time configs.
config.set_intra_op_parallelism_threads(1)
config.set_synchronous_execution(False)
config.set_intra_op_parallelism_threads(2)

config.set_synchronous_execution(True)
self.assertTrue(config.get_synchronous_execution())
self.assertEqual(context.SYNC, context.context().execution_mode)
config.set_synchronous_execution(False)
self.assertFalse(config.get_synchronous_execution())
self.assertEqual(context.ASYNC, context.context().execution_mode)
