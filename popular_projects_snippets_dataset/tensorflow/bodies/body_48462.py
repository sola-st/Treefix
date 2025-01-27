# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Convert a traced (composite)tensor to a representative KerasTensor."""
if isinstance(tensor, ops.Tensor):
    name = getattr(tensor, 'name', None)
    type_spec = type_spec_module.type_spec_from_value(tensor)
    inferred_value = None
    if (type_spec.dtype == dtypes.int32 and type_spec.shape.rank is not None
        and type_spec.shape.rank < 2):
        # If this tensor might be representing shape information,
        # (dtype=int32, rank of 0 or 1, not too large to represent a shape)
        # we attempt to capture any value information tensorflow's
        # shape handling can extract from the current scratch graph.
        #
        # Even though keras layers each trace in their own scratch
        # graph, this shape value info extraction allows us to capture
        # a sizable and useful subset of the C++ shape value inference TF can do
        # if all tf ops appear in the same graph when using shape ops.
        #
        # Examples of things this cannot infer concrete dimensions for
        # that the full single-graph C++ shape inference sometimes can are:
        # * cases where the shape tensor is cast out of int32 before being
        #   manipulated w/ floating point numbers then converted back
        # * cases where int32 tensors w/ rank >= 2 are manipulated before being
        #   used as a shape tensor
        # * cases where int32 tensors too large to represent shapes are
        #   manipulated to a smaller size before being used as a shape tensor
        inferred_value = array_ops.ones(shape=tensor).shape
        if inferred_value.dims:
            inferred_value = inferred_value.as_list()
            if len(inferred_value) > _MAX_TENSOR_RANK:
                inferred_value = None
        else:
            inferred_value = None

    exit(KerasTensor(type_spec, inferred_value=inferred_value, name=name))
else:
    # Fallback to the generic arbitrary-typespec KerasTensor
    name = getattr(tensor, 'name', None)
    type_spec = type_spec_module.type_spec_from_value(tensor)
    exit(cls(type_spec, name=name))
