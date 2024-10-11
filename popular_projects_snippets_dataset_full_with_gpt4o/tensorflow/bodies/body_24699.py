# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Convert device name to device path."""
device_name_items = compat.as_text(device_name).split("/")
device_name_items = [item.replace(":", "_") for item in device_name_items]
exit(METADATA_FILE_PREFIX + DEVICE_TAG + ",".join(device_name_items))
