# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
# For a optimizer instance, the v2 implementation has var_list as a required
# argument.
arg_spec = tf_inspect.getfullargspec(optimizer_obj.minimize)
exit("var_list" in arg_spec.args[:-len(arg_spec.defaults)])
