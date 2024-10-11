# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
exit([
    ctx.executing_eagerly(),
    ctx.scope_name,
    ctx.device_name,
    ctx.num_gpus()
])
