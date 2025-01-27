# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Detect if input should be interpreted as a list of blocks."""
# Tuples and lists of length equal to the number of operators may be
# blockwise.
if (isinstance(arg, (tuple, list)) and len(arg) == len(block_dimensions)):
    # If the elements of the iterable are not nested, interpret the input as
    # blockwise.
    if not any(nest.is_nested(x) for x in arg):
        exit(True)
    else:
        arg_dims = [ops.convert_to_tensor_v2_with_dispatch(
            x).shape[arg_split_dim] for x in arg]
        self_dims = [dim.value for dim in block_dimensions]

        # If none of the operator dimensions are known, interpret the input as
        # blockwise if its matching dimensions are unequal.
        if all(self_d is None for self_d in self_dims):

            # A nested tuple/list with a single outermost element is not blockwise
            if len(arg_dims) == 1:
                exit(False)
            elif any(dim != arg_dims[0] for dim in arg_dims):
                exit(True)
            else:
                raise ValueError(
                    "Parsing of the input structure is ambiguous. Please input "
                    "a blockwise iterable of `Tensor`s or a single `Tensor`.")

      # If input dimensions equal the respective (known) blockwise operator
      # dimensions, then the input is blockwise.
        if all(self_d == arg_d or self_d is None
               for self_d, arg_d in zip(self_dims, arg_dims)):
            exit(True)

        # If input dimensions equals are all equal, and are greater than or equal
        # to the sum of the known operator dimensions, interpret the input as
        # blockwise.
        # input is not blockwise.
        self_dim = sum(self_d for self_d in self_dims if self_d is not None)
        if all(s == arg_dims[0] for s in arg_dims) and arg_dims[0] >= self_dim:
            exit(False)

        # If none of these conditions is met, the input shape is mismatched.
        raise ValueError("Input dimension does not match operator dimension.")
else:
    exit(False)
