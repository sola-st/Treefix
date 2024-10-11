# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(3.)
root.v2 = variables.Variable(2.)
root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
exit(root)
