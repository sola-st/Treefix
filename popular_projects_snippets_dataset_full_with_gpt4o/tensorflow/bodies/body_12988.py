# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Wraps user inputs to support composite tensors for `py_function`.

  1. Flattens `inp` to a list of Tensors (by flattening any composite tensors).
  2. Creates a wrapper fuction for `func` that expects flat inputs and:
     - Packs the inputs into the input structure expected by `func`.
     - Calls `func` with the packed inputs.
     - Checks that `func`'s output matches `Tout`.
     - Flattens func`'s output to a list of Tensors (flattening any composite
       tensors).

  Args:
    func: The function to wrap (`func` argument to `py_function`).
    inp: The input arguments for func (`inp` argument to `py_function`).
    Tout: The expected output types for func (`Tout` argument to `py_function).

  Returns:
    A tuple `(func, inp, Tout, out_structure)`, where `func` is the wrapped
    function, `inp` is the flattened inputs, `Tout` is the list of expected
    dtypes for the flattened outputs, and `out_structure` is the expected
    output structure (which can be used to pack the output tensors).
  """
in_structure = [
    v if isinstance(v, composite_tensor.CompositeTensor) else 1 for v in inp
]
inp = nest.flatten_up_to(in_structure, inp, expand_composites=True)
out_structure = Tout
Tout = [
    v.dtype if isinstance(v, tensor_spec.TensorSpec) else v
    for v in nest.flatten(Tout, expand_composites=True)
]

def wrapped_func(*flat_inp):
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

exit((wrapped_func, inp, Tout, out_structure))
