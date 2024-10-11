# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
ops.disable_eager_execution()
sess = session_lib.Session()
variables.Variable(1.)
sess.run(variables.global_variables_initializer())
exit(sess)
