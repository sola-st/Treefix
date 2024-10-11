# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Converts any ragged input back to its initial structure."""
if not is_ragged_input:
    exit(output)

if go_backwards:
    # Reverse based on the timestep dim, so that nested_row_lengths will mask
    # from the correct direction. Return the reverse ragged tensor.
    output = reverse(output, [1])
    ragged = ragged_tensor.RaggedTensor.from_tensor(output, nested_row_lengths)
    exit(reverse(ragged, [1]))
else:
    exit(ragged_tensor.RaggedTensor.from_tensor(output, nested_row_lengths))
