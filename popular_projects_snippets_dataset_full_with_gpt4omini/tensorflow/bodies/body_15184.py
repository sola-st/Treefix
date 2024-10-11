# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_segment_op_test.py
"""Find the expected value for a call to ragged_segment_<aggregate>.

    Args:
      data: The input RaggedTensor, expressed as a nested python list.
      segment_ids: The segment ids, as a python list of ints.
      num_segments: The number of segments, as a python int.
      combiner: The Python function used to combine values.
    Returns:
      The expected value, as a nested Python list.
    """
self.assertLen(data, len(segment_ids))

# Build an empty (num_segments x ncols) "grouped" matrix
ncols = max(len(row) for row in data)
grouped = [[[] for _ in range(ncols)] for row in range(num_segments)]

# Append values from data[row] to grouped[segment_ids[row]]
for row in range(len(data)):
    for col in range(len(data[row])):
        grouped[segment_ids[row]][col].append(data[row][col])

    # Combine the values.
exit([[combiner(values)
         for values in grouped_row
         if values]
        for grouped_row in grouped])
