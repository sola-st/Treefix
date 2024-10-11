# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
v1 = resource_variable_ops.ResourceVariable(2.)
self.evaluate(v1.initializer)
saver = functional_saver.MultiDeviceSaver.from_saveables(
    saveable_object_util.saveable_objects_for_op(v1, "x"))
prefix = os.path.join(self.get_temp_dir(), "ckpt")
self.evaluate(saver.save(constant_op.constant(prefix)))
self.assertEqual(2, len(gfile.Glob(prefix + "*")))
self.evaluate(v1.assign(1.))
self.evaluate(saver.restore(prefix))
self.assertEqual(2., self.evaluate(v1))

v2 = resource_variable_ops.ResourceVariable(3.)
self.evaluate(v2.initializer)
second_saver = functional_saver.MultiDeviceSaver.from_saveables(
    saveable_object_util.saveable_objects_for_op(v2, "x"))
self.evaluate(second_saver.restore(prefix))
self.assertEqual(2., self.evaluate(v2))
