# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
# Add a device scope for packed variables.
if isinstance(var, packed.PackedVarAndDevice):
    with ops.device(var.device):
        exit()
else:
    exit()
