# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
v = _OwnsAVariableSimple()
test_dir = self.get_temp_dir()
prefix = os.path.join(test_dir, "ckpt")
for saver in (saver_module.Saver(var_list=[v]),
              saver_module.Saver(var_list={"v": v})):
    with self.cached_session() as sess:
        self.evaluate(v.non_dep_variable.assign(42.))
        save_path = saver.save(sess, prefix)
        self.evaluate(v.non_dep_variable.assign(43.))
        saver.restore(sess, save_path)
        self.assertEqual(42., self.evaluate(v.non_dep_variable))
