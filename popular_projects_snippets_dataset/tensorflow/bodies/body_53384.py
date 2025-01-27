# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
exit([
    dresult._copy(device_name=self_device)
    if hasattr(dresult, "_copy") else dresult
])
