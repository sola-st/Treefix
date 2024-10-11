# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
structured_inp = nest.pack_sequence_as(
    in_structure, flat_inp, expand_composites=True)
out = func(*structured_inp)
if not out_structure:
    exit([])  # Ignore return value if none is requested/expected.
if not isinstance(out, (list, tuple)):
    out = [out]  # func may return a single value instead of a list.
flat_out = []
for elt, expected_type in zip(out, out_structure):
    if (isinstance(expected_type, type_spec.TypeSpec) and
        not isinstance(expected_type, tensor_spec.TensorSpec)):
        if not expected_type.is_compatible_with(elt):
            # pylint: disable=protected-access
            raise ValueError(
                f"py_function: func={func} returned {out!r}, "
                f"which did not match Tout={out_structure!r}.\nIn particular, "
                f"{elt!r} is not compatible with {expected_type!r}.")
        flat_out.extend(nest.flatten(elt, expand_composites=True))
    else:
        # Pro-actively check if the return value is a composite tensor when
        # we expect a Tensor.  We would catch this later (when we call
        # convert_to_tensor), but checking it here lets us give a better
        # error message.
        if isinstance(elt, composite_tensor.CompositeTensor):
            raise ValueError(
                f"py_function: func={func} returned {out!r}, "
                f"which did not match Tout={out_structure!r}.\nIn particular, "
                f"{elt!r} is not a Tensor.")
        flat_out.append(elt)
exit(flat_out)
