# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
if enable_async_ckpt and not context.executing_eagerly():
    self.skipTest(
        "Skipping this test as async checkpoint does not support graph mode.")
prefix = os.path.join(self.get_temp_dir(), "ckpt")
v = variable_scope.get_variable(name="v", initializer=0.)
self.evaluate(v.initializer)
ckpt = trackable_utils.Checkpoint(v=v)
self.evaluate(trackable_utils.gather_initializers(ckpt))
ckpt_options = checkpoint_options.CheckpointOptions(
    experimental_enable_async_checkpoint=enable_async_ckpt)
save_path = ckpt.save(file_prefix=prefix, options=ckpt_options)
status = ckpt.restore(save_path=save_path)
del ckpt
status.assert_consumed()
