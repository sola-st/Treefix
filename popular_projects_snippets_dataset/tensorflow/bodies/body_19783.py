# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Reads the event file written by tensor tracer.

  This can be used to read the full tensors written into binary event files by
  by TensorTracer with trace_mode=full_tensor_summary.

  Example usage:
    result_dict_list = tensor_tracer.read_tensor_tracer_event_file(
      event_file_path)
    for result_dict in result_dict_list:
      for step, tensor_dict in result_dict.items():
        for tensor_name, full_tensor_content in tensor_dict.items():
          logging.info(tensor_name, full_tensor_content)

  Args:
    event_file: Path to the event file that contains only tensor tracer events.
  Returns:
    A list of event dictionaries, each of which with the form:
    {step_number: {tensor_name: tensor_content}}. This is a list instead of
    a single event dictionary because it is possible that an event file may
    have multiple event traces, each of them covering the same step ranges.
  Raises:
    ValueError: If an unexpected trace is found.
  """

# Keeps track of how many times that a step number shows up in these events.
step_occurrence_count = collections.defaultdict(int)

# List of step occurrences.
step_occurrence_list = []

for trace_event in summary_iterator.summary_iterator(event_file):
    # First event is an event with file_version: "brain.Event:2"
    if not trace_event.HasField('summary'):
        continue
    if len(trace_event.summary.value) != 1:
        raise ValueError('Single step contains %d summary values,'
                         ' expected 1.' % len(trace_event.summary.value))
    step = trace_event.step
    step_occurrence_count[step] += 1  # a new occurrence for this step.

    occurrence_idx = step_occurrence_count[step] - 1
    occurrence_size = len(step_occurrence_list)

    if occurrence_idx == occurrence_size:
        # This particular occurrence isn't yet recorded on step_occurrence_list.
        # So append this new occurrence to the end of step_occurrence_list.
        new_occurrence = collections.defaultdict(dict)
        step_occurrence_list.append(new_occurrence)
    else:
        # This particular occurrence must be already recorded on
        # step_occurrence_list (i.e. occurrence_idx < occurrence_size).
        if occurrence_idx > occurrence_size:
            raise ValueError('Unexpected: occurrence_idx (%d) > '
                             'occurrence_size (%d)' % (occurrence_idx,
                                                       occurrence_size))
    tensor_value = trace_event.summary.value[0]
    tensor_name = tensor_value.tag

    real_shape = [d.size for d in tensor_value.tensor.tensor_shape.dim]
    tensor_content = np.frombuffer(
        tensor_value.tensor.tensor_content,
        dtypes.DType(tensor_value.tensor.dtype).as_numpy_dtype()
        ).reshape(real_shape)
    step_occurrence_list[occurrence_idx][step][tensor_name] = tensor_content
exit(step_occurrence_list)
