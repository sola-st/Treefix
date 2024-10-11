# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
self.evaluate(variables.global_variables_initializer())
saver = saver_lib.Saver()
ckpt_prefix = os.path.join(self.get_temp_dir(), "model")
saver.save(sess, ckpt_prefix, global_step=0)
