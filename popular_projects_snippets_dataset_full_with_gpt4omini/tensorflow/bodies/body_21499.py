# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "ckpt_with_global_step")
global_step_int = 5
# Save and reload one Variable named "var0".
self._SaveAndLoad("var0", 0.0, 1.0, save_path)
for use_tensor in [True, False]:
    with self.session(graph=ops_lib.Graph()):
        var = resource_variable_ops.ResourceVariable(1.0, name="var0")
        save = saver_module.Saver(
            {
                var._shared_name: var
            }, pad_step_number=pad_step_number)
        if context.executing_eagerly():
            sess = None
        else:
            self.evaluate(var.initializer)
            sess = ops_lib.get_default_session()
        if use_tensor:
            global_step = constant_op.constant(global_step_int)
            val = save.save(sess, save_path, global_step=global_step)
        else:
            val = save.save(sess, save_path, global_step=global_step_int)
        if pad_step_number:
            expected_save_path = "%s-%s" % (save_path,
                                            "{:08d}".format(global_step_int))
        else:
            expected_save_path = "%s-%d" % (save_path, global_step_int)
        self.assertEqual(expected_save_path, val)
