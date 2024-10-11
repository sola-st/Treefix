# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Verify the correctness of the stack frames.

    Currently, it simply asserts that the current file is found in the stack
    frames.
    TODO(cais): Perhaps implement a stricter check later.

    Args:
      stack_frames: The stack frames to verify.
    """
self.assertTrue([
    frame for frame in stack_frames if frame[0] == _current_file_full_path])
