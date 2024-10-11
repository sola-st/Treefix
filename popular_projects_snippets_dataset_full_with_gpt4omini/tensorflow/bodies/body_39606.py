# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
if enable_async_ckpt and not context.executing_eagerly():
    self.skipTest(
        "Skipping this test as async checkpoint does not support graph mode.")
v = _OwnsMirroredVariables()
checkpoint = trackable_utils.Checkpoint(v=v)
test_dir = self.get_temp_dir()
prefix = os.path.join(test_dir, "ckpt")
self.evaluate(v.non_dep_variable.assign(42.))
ckpt_options = checkpoint_options.CheckpointOptions(
    experimental_enable_async_checkpoint=enable_async_ckpt)
save_path = checkpoint.save(file_prefix=prefix, options=ckpt_options)
# TODO(chienchunh): Identify why sync needs to be called here.
if enable_async_ckpt:
    checkpoint._async_checkpointer().sync()
self.evaluate(v.non_dep_variable.assign(43.))
self.evaluate(v.mirrored.assign(44.))
checkpoint.restore(save_path).assert_consumed().initialize_or_restore()
self.assertEqual(42., self.evaluate(v.non_dep_variable))
self.assertEqual(42., self.evaluate(v.mirrored))
self.evaluate(v.non_dep_variable.assign(44.))
save_path = checkpoint.save(file_prefix=prefix, options=ckpt_options)
# TODO(chienchunh): Identify why sync needs to be called here.
if enable_async_ckpt:
    checkpoint._async_checkpointer().sync()
self.evaluate(v.non_dep_variable.assign(45.))
checkpoint.restore(save_path).assert_consumed().initialize_or_restore()
self.assertEqual(44., self.evaluate(v.non_dep_variable))
self.assertEqual(44., self.evaluate(v.mirrored))
