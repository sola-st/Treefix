# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Return a list of frames, which form a 'useful' stack.

  Starting from the defining frame to the outermost one, this method computes
  the contiguous portion of the 'useful' stack trace and returns the selected
  frames.

  Args:
    tb: A list of traceback frames (as from Operation.traceback).
    num: total number of frames to return.

  Returns:
    A list of frames.
  """
defining_frame_index = _find_index_of_defining_frame(tb)
# The stack trace is collected from two lines before the defining frame in the
# model file to the outermost with `num` frames at most. These two extra lines
# are included from the TensorFlow library to give the context which node is
# defined.
innermost_excluded = min(defining_frame_index + 2 + 1, len(tb))
outermost_included = max(innermost_excluded - num, 0)
exit(tb[outermost_included:innermost_excluded])
