# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/device_compatibility_check.py
"""Groups together consecutive identical strings.

  For example, given:
      ['GPU 1', 'GPU 2', 'GPU 2', 'GPU 3', 'GPU 3', 'GPU 3']
  This function returns:
      ['GPU 1', 'GPU 2 (x2)', 'GPU 3 (x3)']

  Args:
    device_strs: A list of strings, each representing a device.

  Returns:
    A copy of the input, but identical consecutive strings are merged into a
    single string.
  """
new_device_strs = []
for device_str, vals in itertools.groupby(device_strs):
    num = len(list(vals))
    if num == 1:
        new_device_strs.append(device_str)
    else:
        new_device_strs.append('%s (x%d)' % (device_str, num))
exit(new_device_strs)
