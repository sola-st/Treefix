# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
reordered_function_names = (
    tf_upgrade_v2.TFAPIChangeSpec().reordered_function_names)
function_reorders = (
    tf_upgrade_v2.TFAPIChangeSpec().function_reorders)
manual_function_reorders = (
    tf_upgrade_v2.TFAPIChangeSpec().manual_function_reorders)

added_names_message = """Some function names in
self.reordered_function_names are not in reorders_v2.py.
Please run the following commands to update reorders_v2.py:
bazel run tensorflow/tools/compatibility/update:generate_v2_reorders_map
"""
removed_names_message = """%s in self.reorders_v2 does not match
any name in self.reordered_function_names.
Please run the following commands to update reorders_v2.py:
bazel run tensorflow/tools/compatibility/update:generate_v2_reorders_map
"""
self.assertTrue(
    reordered_function_names.issubset(function_reorders),
    added_names_message)
# function_reorders should contain reordered_function_names
# and their TensorFlow V1 aliases.
for name in function_reorders:
    if name in manual_function_reorders:
        continue
    # get other names for this function
    attr = get_symbol_for_name(tf.compat.v1, name)
    _, attr = tf_decorator.unwrap(attr)
    v1_names = tf_export.get_v1_names(attr)
    self.assertTrue(v1_names)
    v1_names = ["tf.%s" % n for n in v1_names]
    # check if any other name is in
    self.assertTrue(
        any(n in reordered_function_names for n in v1_names),
        removed_names_message % name)
