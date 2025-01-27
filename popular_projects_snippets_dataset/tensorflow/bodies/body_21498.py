# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "variables_reshape")
with session.Session("", graph=ops_lib.Graph()) as sess:
    var = variables.VariableV1([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    init = variables.global_variables_initializer()
    save = saver_module.Saver()
    init.run()
    save.save(sess, save_path)

# Error when restoring with default reshape=False
with session.Session("", graph=ops_lib.Graph()) as sess:
    var = variables.VariableV1([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    save = saver_module.Saver()
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Assign requires shapes of both tensors to match."):
        save.restore(sess, save_path)

    # Restored to new shape with reshape=True
with session.Session("", graph=ops_lib.Graph()) as sess:
    var = variables.VariableV1([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
    save = saver_module.Saver(reshape=True)
    save.restore(sess, save_path)
    self.assertAllClose([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
                        self.evaluate(var))
