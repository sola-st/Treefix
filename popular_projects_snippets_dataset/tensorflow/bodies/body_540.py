# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
new_name = full_name.replace("tf.", "tf.compat.v1.", 1)
exit(_rename_func(node, full_name, new_name, logs, reason))
