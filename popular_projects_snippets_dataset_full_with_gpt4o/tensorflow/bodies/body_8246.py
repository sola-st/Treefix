# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py

if (isinstance(distribution,
               collective_all_reduce_strategy.CollectiveAllReduceStrategy)
    and mode == "graph"):
    self.skipTest("MWMS combinations tests do not work well in graph mode.")

with distribution.scope():
    v = variables_lib.Variable(
        constant_op.constant([1., 2., 3., 4]),
        synchronization=synchronization,
        aggregation=aggregation)

self.evaluate(v.initializer)
before_save = self.evaluate(v.read_value())

# Save random weights into checkpoint.
checkpoint = trackable_utils.Checkpoint(v=v)
prefix = os.path.join(self.get_temp_dir(), "ckpt")
with self.test_session():
    save_path = checkpoint.save(prefix)

# Assign inverted value.
self.evaluate(v.assign(constant_op.constant([4., 3., 2., 1.])))
after_assign = self.evaluate(v.read_value())
self.assertNotAllClose(before_save, after_assign)

# Restore from the checkpoint.
with self.test_session():
    checkpoint.restore(save_path).assert_consumed().run_restore_ops()
after_restore = self.evaluate(v)
self.assertAllClose(before_save, after_restore)
