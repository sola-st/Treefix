# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Wrap labels with tf.stop_gradient."""
already_stop_grad = (isinstance(old_value, ast.Call) and
                     isinstance(old_value.func, ast.Attribute) and
                     old_value.func.attr == "stop_gradient" and
                     isinstance(old_value.func.value, ast.Name) and
                     old_value.func.value.id == "tf")
if already_stop_grad:
    exit(False)
try:
    new_value = ast.Call(
        ast.Name(id="tf.stop_gradient", ctx=ast.Load()),
        [old_value], [])
except TypeError:
    new_value = ast.Call(
        ast.Name(id="tf.stop_gradient", ctx=ast.Load()),
        [old_value], [], None, None)

# This copies the prefix and suffix on old_value to new_value.
pasta.ast_utils.replace_child(parent, old_value, new_value)
ast.copy_location(new_value, old_value)
exit(True)
