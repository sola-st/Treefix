# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format.py
prev_ind = None
for ind in indices_list:
    # Check indices match tensor dimensions.
    dims = formatted.annotations["tensor_metadata"]["shape"]
    if len(ind) != len(dims):
        raise ValueError("Dimensions mismatch: requested: %d; actual: %d" %
                         (len(ind), len(dims)))

    # Check indices is within size limits.
    for req_idx, siz in zip(ind, dims):
        if req_idx >= siz:
            raise ValueError("Indices exceed tensor dimensions.")
        if req_idx < 0:
            raise ValueError("Indices contain negative value(s).")

    # Check indices are in ascending order.
    if prev_ind and ind < prev_ind:
        raise ValueError("Input indices sets are not in ascending order.")

    prev_ind = ind
