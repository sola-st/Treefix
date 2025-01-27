# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
if enable_async_ckpt and not context.executing_eagerly():
    self.skipTest(
        "Skipping this test as async checkpoint does not support graph mode.")
checkpoint = trackable_utils.Checkpoint(
    a=[variables_lib.Variable(0.), variables_lib.Variable(1.)],
    b={"a": variables_lib.Variable(2.), "b": variables_lib.Variable(3.)})
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
ckpt_options = checkpoint_options.CheckpointOptions(
    experimental_enable_async_checkpoint=enable_async_ckpt)
save_path = checkpoint.save(file_prefix=checkpoint_prefix,
                            options=ckpt_options)
load_checkpoint = trackable_utils.Checkpoint(
    a=[variables_lib.Variable(4.), variables_lib.Variable(5.)],
    b={"a": variables_lib.Variable(6.), "b": variables_lib.Variable(7.)})
# When async checkpoint is enabled, we need to first make sure that the
# checkpoint saving is fully complete before the checkpoint file can be
# loaded by another checkpoint instance. Calling checkpoint.restore() is a
# trick to make sure its async thread is joined.
if enable_async_ckpt:
    checkpoint.restore(save_path)
load_checkpoint.restore(save_path)
self.assertAllClose(self.evaluate(load_checkpoint.a), [0, 1])
self.assertAllClose(self.evaluate(load_checkpoint.b), {"a": 2, "b": 3})
