# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
sess = session.Session()
sess.run(variables_lib.global_variables_initializer())
sess.run(lookup_ops.tables_initializer())
exit(sess)
