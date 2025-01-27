# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py
trace = tf_stack.extract_stack()  # COMMENT
frame = trace.last_user_frame()
self.assertRegex(frame.line, "# COMMENT")
