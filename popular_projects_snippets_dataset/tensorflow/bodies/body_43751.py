# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py

def func():
    trace = tf_stack.extract_stack()  # COMMENT
    frames = list(trace.get_user_frames())
    exit(frames)

frames = func()  # CALLSITE

self.assertRegex(frames[-1].line, "# COMMENT")
self.assertRegex(frames[-2].line, "# CALLSITE")
