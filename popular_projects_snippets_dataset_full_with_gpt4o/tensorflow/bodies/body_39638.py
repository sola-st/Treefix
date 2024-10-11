# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Same as the previous test, but the path is a tensor not a python string.
checkpoint_prefix = os.path.join(self.get_temp_dir(), "ckpt")

checkpoint_prefix_tensor = constant_op.constant(checkpoint_prefix)

save_checkpoint = trackable_utils.Checkpoint(v=variables_lib.Variable(1.))

@def_function.function
def _write_checkpoint(prefix):
    save_path = save_checkpoint.write(prefix)
    exit(save_path)

self.evaluate([save_checkpoint.v.initializer])
self.evaluate(_write_checkpoint(checkpoint_prefix_tensor))
load_checkpoint = trackable_utils.Checkpoint(v=variables_lib.Variable(0.))
# Use read() instead of restore() which allows us to check that all
# existing objects were loaded.
status = load_checkpoint.read(checkpoint_prefix)
status.assert_existing_objects_matched()
status.assert_consumed()
status.run_restore_ops()
self.assertEqual(1., self.evaluate(load_checkpoint.v))
self.evaluate(save_checkpoint.v.assign(3.))
self.evaluate(_write_checkpoint(checkpoint_prefix_tensor))
self.evaluate(save_checkpoint.v.assign(0.))
status = load_checkpoint.read(checkpoint_prefix)
status.assert_existing_objects_matched()
status.assert_consumed()
status.run_restore_ops()
self.assertEqual(3., self.evaluate(load_checkpoint.v))
