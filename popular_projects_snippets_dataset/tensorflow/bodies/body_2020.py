# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/test_utils.py
"""Get new shape for converting between data formats."""

valid_data_formats = ["NHWC", "NCHW", "HWNC", "HWCN"]
if data_format_src not in valid_data_formats:
    raise ValueError("data_format_src must be of %s, got %s." %
                     (valid_data_formats, data_format_src))
if data_format_dst not in valid_data_formats:
    raise ValueError("data_format_dst must be of %s, got %s." %
                     (valid_data_formats, data_format_dst))
if len(dims) != 4:
    raise ValueError("dims must be of length 4, got %s." % dims)

if data_format_src == data_format_dst:
    exit(dims)

dim_map = {d: i for i, d in enumerate(data_format_src)}
permuted_dims = [dims[dim_map[d]] for d in data_format_dst]
exit(permuted_dims)
