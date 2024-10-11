# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Generates a new model byte array after deduplicating readonly buffers.

  This function should be invoked after the model optimization toolkit. The
  model optimization toolkit assumes that each tensor object owns its each
  buffer separately.

  Args:
    tflite_model: TFLite flatbuffer in a byte array to be deduplicated.

  Returns:
    TFLite flatbuffer in a bytes array, processed with the deduplication method.
  """
# Load TFLite Flatbuffer byte array into an object.
model = flatbuffer_utils.convert_bytearray_to_object(tflite_model)

# Get all the read-only buffers, which can be modified without causing any
# issue in the graph invocation stage.
read_only_buffer_indices = set()
for subgraph in model.subgraphs:
    # To get all the read-only buffers:
    # (1) Get all read-only input tensors.
    # (2) Discard intermediate or output tensors.
    # (3) Discard the subgraph's input/output tensors.
    # (4) Gather the buffers of the read-only input tensors.

    # (1) Get read-only input tensors.
    read_only_input_tensor_indices = set()
    for op in subgraph.operators:
        if op.inputs is None:
            continue
        for i, input_tensor_idx in enumerate(op.inputs):
            # Ignore mutable tensors.
            if op.mutatingVariableInputs is not None:
                # Ignore invalid tensors.
                if (i < len(op.mutatingVariableInputs) and
                    op.mutatingVariableInputs[i]):
                    continue
        # Ignore variable tensors.
            if subgraph.tensors[input_tensor_idx].isVariable:
                continue
            read_only_input_tensor_indices.add(input_tensor_idx)

    # (2) Discard intermediate or output tensors.
    for op in subgraph.operators:
        if op.outputs is not None:
            for output_tensor_idx in op.outputs:
                read_only_input_tensor_indices.discard(output_tensor_idx)
        if op.intermediates is not None:
            for intermediate_tensor_idx in op.intermediates:
                read_only_input_tensor_indices.discard(intermediate_tensor_idx)

    # (3) Discard the subgraph's input and output tensors.
    if subgraph.inputs is not None:
        for input_tensor_idx in subgraph.inputs:
            read_only_input_tensor_indices.discard(input_tensor_idx)
    if subgraph.outputs is not None:
        for output_tensor_idx in subgraph.outputs:
            read_only_input_tensor_indices.discard(output_tensor_idx)

    # (4) Gather the buffers of the read-only input tensors.
    for tensor_idx in read_only_input_tensor_indices:
        read_only_buffer_indices.add(subgraph.tensors[tensor_idx].buffer)

  # Ignore invalid negative index or zero-sized buffers.
for buffer_idx in read_only_buffer_indices.copy():
    if (buffer_idx < 0 or (model.buffers[buffer_idx].data is None or
                           isinstance(model.buffers[buffer_idx].data, list) or
                           model.buffers[buffer_idx].data.size == 0)):
        read_only_buffer_indices.discard(buffer_idx)

class BufferIndex:
    """A class to store index, size, hash of the buffers in TFLite model."""

    def __init__(self, idx, size, hash_value):
        self.idx = idx
        self.size = size
        self.hash_value = hash_value

read_only_buffers = list(
    map(
        lambda index: BufferIndex(  # pylint: disable=g-long-lambda
            index, model.buffers[index].data.size,
            hashlib.md5(model.buffers[index].data.data.tobytes()).hexdigest()
        ),
        read_only_buffer_indices))

# Sort read_only_buffers by buffer size & hash in descending order.
read_only_buffers = sorted(
    read_only_buffers,
    key=lambda buffer: (buffer.size, buffer.hash_value),
    reverse=True)

# Create a map of duplicate buffers (same size and same type).
# eg: In [1, 2, 3, 4, 5, 6] if (1, 4, 6) and (2, 5) are each, groups of buffer
# indices of the same size and type, then the map would be {4:1, 6:1, 5:2}
duplicate_buffer_map = {}
for i, buffer_i in enumerate(read_only_buffers):
    # This buffer is a duplicate.
    if buffer_i.idx in duplicate_buffer_map:
        continue
    # This buffer is unique. Scan rest of the list to find duplicates
    # of this buffer and mark them accordingly.
    for buffer_j in read_only_buffers[i + 1:]:
        if buffer_j.idx in duplicate_buffer_map:
            continue
        if buffer_i.size != buffer_j.size:
            break
        if buffer_i.hash_value != buffer_j.hash_value:
            continue
        # Found duplicate. Nullify j-th buffer and use i-th buffer instead.
        duplicate_buffer_map[buffer_j.idx] = buffer_i.idx

  # Make the duplicated tensors use the single shared buffer index.
for subgraph in model.subgraphs:
    for op in subgraph.operators:
        if op.inputs is None:
            continue
        for input_tensor in op.inputs:
            buffer_idx = subgraph.tensors[input_tensor].buffer
            if buffer_idx in duplicate_buffer_map:
                subgraph.tensors[input_tensor].buffer = (
                    duplicate_buffer_map[buffer_idx])

  # Nullify the unused buffers.
for idx in duplicate_buffer_map:
    model.buffers[idx].data = None

# Return a TFLite flatbuffer as a byte array.
exit(flatbuffer_utils.convert_object_to_bytearray(model))
