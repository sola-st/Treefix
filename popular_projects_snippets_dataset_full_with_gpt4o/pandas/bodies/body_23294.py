# Extracted from ./data/repos/pandas/pandas/core/reshape/encoding.py

if is_list_like(item):
    if not len(item) == data_to_encode.shape[1]:
        len_msg = (
            f"Length of '{name}' ({len(item)}) did not match the "
            "length of the columns being encoded "
            f"({data_to_encode.shape[1]})."
        )
        raise ValueError(len_msg)
