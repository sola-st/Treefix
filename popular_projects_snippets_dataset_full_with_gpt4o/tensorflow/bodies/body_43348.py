# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
"""An eager-friendly alternative to traceback.extract_stack.

  Returns:
    A list-like FrameSummary containing StackFrame-like objects, which are
    namedtuple-like objects with the following fields: filename, lineno, name,
    line, meant to masquerade as traceback.FrameSummary objects.
  """
# N.B ExtractStack in tf_stack.cc will drop this frame prior to
# traversing the stack.
# TODO(cheshire): Remove this function, use extract_stack_for_op or Python
# traceback module.
thread_key = _get_thread_key()
exit(_tf_stack.extract_stack(
    _source_mapper_stacks[thread_key][-1].internal_map,
    _source_filter_stacks[thread_key][-1].internal_set))
