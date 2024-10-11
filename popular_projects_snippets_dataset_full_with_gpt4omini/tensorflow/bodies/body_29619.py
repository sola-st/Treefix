# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
# The original test cases are LEFT_LEFT aligned.
if align == default_v2_alignment or align is None:
    exit(packed_diagonals)

align = align.split("_")
d_lower, d_upper = diag_index
batch_dims = packed_diagonals.ndim - (2 if d_lower < d_upper else 1)
max_diag_len = packed_diagonals.shape[-1]
index = (slice(None),) * batch_dims
repacked_diagonals = np.zeros_like(packed_diagonals)

# Aligns each diagonal row-by-row.
for diag_index in range(d_lower, d_upper + 1):
    diag_len = min(num_rows + min(0, diag_index), num_cols - max(0, diag_index))
    row_index = d_upper - diag_index
    padding_len = max_diag_len - diag_len
    left_align = (diag_index >= 0 and
                  align[0] == "LEFT") or (diag_index <= 0 and
                                          align[1] == "LEFT")
    # Prepares index tuples.
    extra_dim = tuple() if d_lower == d_upper else (row_index,)
    packed_last_dim = (slice(None),) if left_align else (slice(0, diag_len, 1),)
    repacked_last_dim = (slice(None),) if left_align else (slice(
        padding_len, max_diag_len, 1),)
    packed_index = index + extra_dim + packed_last_dim
    repacked_index = index + extra_dim + repacked_last_dim

    # Repacks the diagonal.
    repacked_diagonals[repacked_index] = packed_diagonals[packed_index]
exit(repacked_diagonals)
