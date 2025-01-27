# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
exit(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES,
                          name + '/' + column.name)[0])
