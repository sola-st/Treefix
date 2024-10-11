# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_prefix = os.path.join(checkpoint_dir, "model")
checkpoint_state_name = "checkpoint"
v1 = variable_scope.get_variable("var1", [1, 10])
v2 = variable_scope.get_variable("var2", [10, 10])
v3 = variable_scope.get_variable("var3", [100, 100])
with variable_scope.variable_scope("useful_scope"):
    v4 = variable_scope.get_variable("var4", [9, 9])
sess.run(variables.global_variables_initializer())
v1_value, v2_value, v3_value, v4_value = sess.run([v1, v2, v3, v4])
saver = saver_lib.Saver()
saver.save(
    sess,
    checkpoint_prefix,
    global_step=0,
    latest_filename=checkpoint_state_name)
exit((v1_value, v2_value, v3_value, v4_value))
