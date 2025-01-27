# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "variables")
with session.Session("", graph=ops_lib.Graph()) as sess:
    one = variables.VariableV1(1.0)
    twos = variables.VariableV1([2.0, 2.0, 2.0])
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    init = variables.global_variables_initializer()
    save = saver_module.Saver()
    init.run()
    v2.insert("k1", 3.0).run()
    save.save(sess, save_path)

with session.Session("", graph=ops_lib.Graph()) as sess:
    one = variables.VariableV1(0.0)
    twos = variables.VariableV1([0.0, 0.0, 0.0])
    v2 = saver_test_utils.CheckpointedOp(name="v2")
    # Saver with no arg, defaults to 'all variables'.
    save = saver_module.Saver()
    save.restore(sess, save_path)
    self.assertAllClose(1.0, self.evaluate(one))
    self.assertAllClose([2.0, 2.0, 2.0], self.evaluate(twos))
    self.assertEqual(b"k1", self.evaluate(v2.keys()))
    self.assertEqual(3.0, self.evaluate(v2.values()))
