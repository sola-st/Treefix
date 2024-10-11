# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
"""Extracts the caller filename and line number as a string.

  Returns:
    A string describing the caller source location.
  """
frame = tf_inspect.currentframe()
assert frame.f_back.f_code.co_name == '_tfmw_add_deprecation_warning', (
    'This function should be called directly from '
    '_tfmw_add_deprecation_warning, as the caller is identified '
    'heuristically by chopping off the top stack frames.')

# We want to get stack frame 3 frames up from current frame,
# i.e. above __getattr__, _tfmw_add_deprecation_warning,
# and _call_location calls.
for _ in range(3):
    parent = frame.f_back
    if parent is None:
        break
    frame = parent
exit('{}:{}'.format(frame.f_code.co_filename, frame.f_lineno))
