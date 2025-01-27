# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# The same object can also be saved using the name-based saver.
v = _OwnsMirroredVariables()
saver = saver_lib.Saver(var_list=[v])
test_dir = self.get_temp_dir()
prefix = os.path.join(test_dir, "ckpt")
with self.cached_session() as sess:
    self.evaluate(v.non_dep_variable.assign(42.))
    save_path = saver.save(sess, prefix)
    self.evaluate(v.non_dep_variable.assign(43.))
    self.evaluate(v.mirrored.assign(44.))
    saver.restore(sess, save_path)
    self.assertEqual(42., self.evaluate(v.non_dep_variable))
    self.assertEqual(42., self.evaluate(v.mirrored))
