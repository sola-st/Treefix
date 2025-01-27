# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py
trace = tf_stack.extract_stack()  # COMMENT
frames = list(trace.get_user_frames())
exit(frames)
