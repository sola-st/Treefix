# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
small_v = [variable_scope.get_variable(
    "small%d" % i, shape=[10, 2], use_resource=True) for i in range(5)]
large_v = [variable_scope.get_variable(
    "large%d" % i, shape=[32000, 1000], use_resource=True)
           for i in range(3)]
exit(small_v + large_v)
