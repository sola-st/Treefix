# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html.py
if op_name in conversion_log.built_in_ops:
    exit("BUILT-IN")
elif op_name in conversion_log.custom_ops:
    exit("CUSTOM OP")
else:
    exit("SELECT OP")
