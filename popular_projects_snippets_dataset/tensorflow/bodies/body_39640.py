# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Same as the previous test, but the path is a tensor not a python string.
checkpoint_prefix = os.path.join(
    self.get_temp_dir(), "DOES_NOT_EXIST", "ckpt")

checkpoint_prefix_tensor = constant_op.constant(checkpoint_prefix)

save_checkpoint = trackable_utils.Checkpoint(v=variables_lib.Variable(1.))

@def_function.function
def _write_checkpoint(prefix):
    save_path = save_checkpoint.write(prefix)
    exit(save_path)

self.evaluate([save_checkpoint.v.initializer])
with self.assertRaises(errors_impl.NotFoundError):
    self.evaluate(_write_checkpoint(checkpoint_prefix_tensor))
