# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir.py
# TODO(cheshire): This is a hack to get the current "preferred" device,
# there is no current API to get it otherwise.
if device_name is None:
    device_name = random_ops.random_normal([]).device
exit(device_name)
