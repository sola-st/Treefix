# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
sess = session.Session(config=config)
sess.run(variables_lib.global_variables_initializer())
sess.run(lookup_ops.tables_initializer())
exit(sess)
