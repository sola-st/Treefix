# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with self.session(graph=ops_lib.Graph()) as sess:
    var = resource_variable_ops.ResourceVariable(var_value, name=var_name)
    save = saver_module.Saver({var_name: var})
    if not context.executing_eagerly():
        self.evaluate(var.initializer)
    val = save.save(sess, save_path)
    self.assertEqual(save_path, val)
with self.session(graph=ops_lib.Graph()) as sess:
    var = resource_variable_ops.ResourceVariable(other_value, name=var_name)
    save = saver_module.Saver({var_name: var})
    save.restore(sess, save_path)
    self.assertAllClose(var_value, self.evaluate(var))
