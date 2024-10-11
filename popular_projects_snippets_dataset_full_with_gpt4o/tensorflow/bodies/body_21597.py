# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")

with ops_lib.Graph().as_default() as g:
    a = variables.VariableV1(1., name="a")
    a_saver = saver_module.Saver([a])

    with self.session(graph=g) as sess:
        self.evaluate(a.initializer)
        save_path = a_saver.save(sess=sess, save_path=checkpoint_prefix)

with ops_lib.Graph().as_default() as g:
    a = variables.VariableV1([1.], name="a")
    a_saver = saver_module.Saver([a])
    with self.session(graph=g) as sess:
        with self.assertRaisesRegex(
            errors.InvalidArgumentError,
            "a mismatch between the current graph and the graph"):
            a_saver.restore(sess=sess, save_path=save_path)
