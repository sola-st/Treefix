# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
"""Attaches the current stack trace to `c_op`.

  Args:
    c_op: a TF_Operation object.
    stacklevel: An integer for ignoring Python wrapper stack frames.
      The default value of 1 ignores this function from the frame.
  """
# N.B ExtractStack in tf_stack.cc will drop this frame prior to
# traversing the stack.
thread_key = _get_thread_key()
_tf_stack.extract_stack_for_op(
    _source_mapper_stacks[thread_key][-1].internal_map,
    _source_filter_stacks[thread_key][-1].internal_set, c_op, stacklevel)
