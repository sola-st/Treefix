# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack_test.py
# Both defined on the same line to produce identical stacks.
stacks = tf_stack.extract_stack(), traceback.extract_stack()
self.assertEqual(
    traceback.format_list(stacks[0]), traceback.format_list(stacks[1]))
