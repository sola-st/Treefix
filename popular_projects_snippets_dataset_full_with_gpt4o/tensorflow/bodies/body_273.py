# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
full_dict = tf_upgrade_v2.TFAPIChangeSpec().function_arg_warnings
method_names = list(full_dict.keys())
for method_name in method_names:
    args = list(full_dict[method_name].keys())
    if "contrib" in method_name:
        # Skip descending and fetching contrib methods during test. These are
        # not available in the repo anymore.
        continue
    elif method_name.startswith("*."):
        # special case for optimizer methods
        method = method_name.replace("*", "tf.train.Optimizer")
    else:
        method = method_name

    method = get_symbol_for_name(tf, method)
    arg_spec = tf_inspect.getfullargspec(method)
    for (arg, pos) in args:
        # to deal with the self argument on methods on objects
        if method_name.startswith("*."):
            pos += 1
        self.assertEqual(arg_spec[0][pos], arg)
