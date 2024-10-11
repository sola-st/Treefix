# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
with ops.device("cpu:0"):
    v0 = resource_variable_ops.ResourceVariable(0.)
with ops.device("cpu:1"):
    v1 = resource_variable_ops.ResourceVariable(1.)
with ops.device("cpu:2"):
    v2 = resource_variable_ops.ResourceVariable(2.)

self.evaluate([v0.initializer, v1.initializer, v2.initializer])
saver = functional_saver.MultiDeviceSaver.from_saveables(
    list(saveable_object_util.saveable_objects_for_op(v0, "v0")) +
    list(saveable_object_util.saveable_objects_for_op(v1, "v1")) +
    list(saveable_object_util.saveable_objects_for_op(v2, "v2")))
prefix = os.path.join(self.get_temp_dir(), "ckpt")
self.evaluate(saver.save(constant_op.constant(prefix), self.local_options))
self.assertEqual(2, len(gfile.Glob(prefix + "*")))
self.evaluate(v0.assign(-1.))
self.evaluate(v1.assign(-1.))
self.evaluate(v2.assign(-1.))
self.evaluate(
    saver.restore(constant_op.constant(prefix), self.local_options))
self.assertEqual(0., self.evaluate(v0))
self.assertEqual(1., self.evaluate(v1))
self.assertEqual(2., self.evaluate(v2))

# In graph mode, verify that the save and restore ops were set to run on
# localhost.
if not context.executing_eagerly():
    for op in ops.get_default_graph().get_operations():
        if op.type in ("SaveV2", "RestoreV2", "MergeV2Checkpoints"):
            self.assertEqual(LOCALHOST, op.device)
