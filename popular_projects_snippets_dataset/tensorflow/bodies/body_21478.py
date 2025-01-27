# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with context.eager_mode():
    ckpt_prefix = os.path.join(self.get_temp_dir(), "ckpt")

    v1 = resource_variable_ops.ResourceVariable(3.14, name="v1")
    v2 = resource_variable_ops.ResourceVariable([1, 2], name="v2")
    save = saver_module.Saver([v1, v2])
    save.save(None, ckpt_prefix)

    v1.assign(0.0)
    v2.assign([0, 0])
    self.assertNear(0.0, self.evaluate(v1), 1e-5)
    self.assertAllEqual([0, 0], self.evaluate(v2))

    save.restore(None, ckpt_prefix)
    self.assertNear(3.14, self.evaluate(v1), 1e-5)
    self.assertAllEqual([1, 2], self.evaluate(v2))
