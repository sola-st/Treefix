# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
if enable_async_ckpt and not context.executing_eagerly():
    self.skipTest(
        "Skipping this test as async checkpoint does not support graph mode.")
directory = self.get_temp_dir()
prefix = os.path.join(directory, "ckpt")
step = resource_variable_ops.ResourceVariable(0, dtype=dtypes.int64)
checkpoint = trackable_utils.Checkpoint(step=step)
ckpt_options = checkpoint_options.CheckpointOptions(
    experimental_enable_async_checkpoint=enable_async_ckpt)
self.evaluate(step.initializer)
for i in range(5):
    path = checkpoint.write("%s-%d" % (prefix, self.evaluate(step)),
                            options=ckpt_options)
    expected_suffix = "-%d" % (2 * i,)
    if not path.endswith(expected_suffix):
        self.fail("%s should have suffix %s" % (path, expected_suffix))
    self.evaluate(step.assign_add(2))
