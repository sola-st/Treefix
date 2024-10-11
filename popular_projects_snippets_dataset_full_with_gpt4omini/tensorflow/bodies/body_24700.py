# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Parse device name from device path.

  Args:
    device_dir: (str) a directory name for the device.

  Returns:
    (str) parsed device name.
  """
path_items = os.path.basename(device_dir)[
    len(METADATA_FILE_PREFIX) + len(DEVICE_TAG):].split(",")
exit("/".join([
    path_item.replace("device_", "device:").replace("_", ":", 1)
    for path_item in path_items]))
