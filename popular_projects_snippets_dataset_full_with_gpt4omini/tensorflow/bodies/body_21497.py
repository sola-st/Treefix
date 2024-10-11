# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "deferred_build")
with session.Session("", graph=ops_lib.Graph()) as sess:
    one = variables.VariableV1(1.0)
    save = saver_module.Saver(defer_build=True)
    # if build is not deferred, saver cannot save the `twos`.
    twos = variables.VariableV1([2.0, 2.0, 2.0])
    init = variables.global_variables_initializer()
    save.build()
    init.run()
    save.save(sess, save_path)

with session.Session("", graph=ops_lib.Graph()) as sess:
    one = variables.VariableV1(0.0)
    twos = variables.VariableV1([0.0, 0.0, 0.0])
    # Saver with no arg, defaults to 'all variables'.
    save = saver_module.Saver()
    save.restore(sess, save_path)
    self.assertAllClose(1.0, self.evaluate(one))
    self.assertAllClose([2.0, 2.0, 2.0], self.evaluate(twos))
