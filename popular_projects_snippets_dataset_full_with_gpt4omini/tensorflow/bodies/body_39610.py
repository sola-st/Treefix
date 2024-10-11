# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
localhost = "/job:localhost/device:CPU:0"
options = checkpoint_options.CheckpointOptions(
    experimental_io_device=localhost)
prefix = os.path.join(self.get_temp_dir(), "ckpt")
v = variable_scope.get_variable(name="v", initializer=0.)
self.evaluate(v.initializer)
ckpt = trackable_utils.Checkpoint(v=v)
self.evaluate(trackable_utils.gather_initializers(ckpt))
save_path = ckpt.save(file_prefix=prefix, options=options)
status = ckpt.restore(save_path=save_path, options=options)
del ckpt
status.assert_consumed()

# In graph mode, verify that the save and restore ops were set to run on
# localhost.
if not context.executing_eagerly():
    for op in ops.get_default_graph().get_operations():
        if op.type in ("SaveV2", "RestoreV2"):
            self.assertEqual(localhost, op.device)
