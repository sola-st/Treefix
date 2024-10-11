# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
saver = saver_lib.Saver(var_list=[var])
test_dir = self.get_temp_dir()
prefix = os.path.join(test_dir, "ckpt")
exit((saver.save(sess, prefix), saver))
