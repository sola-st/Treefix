# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
name_parts = name.split(".")
symbol = root
# Iterate starting with second item since 1st item is "tf.".
for part in name_parts[1:]:
    symbol = getattr(symbol, part)
exit(symbol)
