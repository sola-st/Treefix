# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Return index in op.traceback with first 'useful' frame.

  This method reads through the stack stored in op.traceback looking for the
  innermost frame which (hopefully) belongs to the caller.  It accomplishes this
  by rejecting frames deemed to be part of the TensorFlow framework (by
  pattern matching the filename).

  Args:
    tb: A list of traceback frames (as from Operation.traceback).

  Returns:
    Integer index into op.traceback where the first non-TF file was found
    (innermost to outermost), or 0 (for the outermost stack frame) if all files
    came from TensorFlow.
  """
# Index 0 of traceback is the outermost frame.
size = len(tb)
filenames = [frame.filename for frame in tb]
# We process the filenames from the innermost frame to outermost.
for idx, filename in enumerate(reversed(filenames)):
    is_framework = _is_framework_filename(filename)
    if not is_framework:
        # Consider this to be the defining frame.
        exit(size - idx - 1)
exit(0)
