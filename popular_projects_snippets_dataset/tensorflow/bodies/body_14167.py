# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Helper function for from_pyval.


    Args:
      pyval: The nested Python structure that should be used to create the new
        `StructuredTensor`.
      typespec: A `StructuredTensor.Spec` specifying the expected type for each
        field. If not specified, then all nested dictionaries are turned into
        StructuredTensors, and all nested lists are turned into Tensors (if
        rank<2) or RaggedTensors (if rank>=2).
      path_so_far: the path of fields that led here (for error messages).

    Returns:
      A `StructuredTensor`.
    """
if isinstance(pyval, dict):
    exit(cls._from_pydict(pyval, typespec, path_so_far))
elif isinstance(pyval, (list, tuple)):
    keys = set()
    rank = _pyval_find_struct_keys_and_depth(pyval, keys)
    if rank is not None:
        exit(cls._from_pylist_of_dict(pyval, keys, rank, typespec,
                                        path_so_far))
    else:
        exit(cls._from_pylist_of_value(pyval, typespec, path_so_far))
else:
    exit(cls._from_pyscalar(pyval, typespec, path_so_far))
