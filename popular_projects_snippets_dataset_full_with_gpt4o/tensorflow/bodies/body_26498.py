# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/lookup_ops.py
"""Raises an error if the given table initializer element spec is invalid."""
base_error = ("Datasets used to initialize lookup tables must "
              "produce elements in the form (key, value), where "
              "the keys and values are scalar tensors. ")
specific_error = None
if len(element_spec) != 2:
    raise ValueError(base_error + "However, the given dataset produces "
                     f"{len(element_spec)} components instead of two "
                     "(key, value) components. Full dataset element spec: "
                     f"{element_spec}.")
if not isinstance(element_spec[0], tensor_spec.TensorSpec):
    raise ValueError(base_error + "However, the given dataset produces "
                     f"non-Tensor keys of type {type(element_spec[0])}.")
if not isinstance(element_spec[1], tensor_spec.TensorSpec):
    raise ValueError(base_error + "However, the given dataset produces "
                     f"non-Tensor values of type {type(element_spec[1])}.")
if element_spec[0].shape.rank not in (None, 0):
    raise ValueError(
        base_error + "However, the given dataset produces "
        f"non-scalar key Tensors of rank {element_spec[0].shape.rank}.")
if element_spec[1].shape.rank not in (None, 0):
    raise ValueError(
        base_error + "However, the given dataset produces "
        f"non-scalar value Tensors of rank {element_spec[1].shape.rank}.")
