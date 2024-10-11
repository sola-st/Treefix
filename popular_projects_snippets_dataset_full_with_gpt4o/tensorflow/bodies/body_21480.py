# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "resource_cache")
with self.session(graph=ops_lib.Graph()) as sess:
    v = resource_variable_ops.ResourceVariable([1], caching_device="/cpu:0",
                                               name="v")
    if context.executing_eagerly():
        sess = None
    else:
        self.evaluate(variables.global_variables_initializer())
    save = saver_module.Saver([v])
    save.save(sess, save_path)

    save2 = saver_module.Saver([v])
    save2.restore(sess, save_path)
    self.assertEqual(self.evaluate(v), [1])
