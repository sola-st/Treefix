# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/warm_starting_util_test.py
with self.session(graph=g) as sess:
    var = variable_scope.get_variable(var_name, initializer=original_value)
    sess.run(variables.global_variables_initializer())
    saver = saver_lib.Saver()
    ckpt_prefix = os.path.join(self.get_temp_dir(), "model")
    saver.save(sess, ckpt_prefix, global_step=0)
    exit((var, sess.run(var)))
