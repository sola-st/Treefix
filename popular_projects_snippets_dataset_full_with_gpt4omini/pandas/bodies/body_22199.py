# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if inference:
    # Check for edge case
    if isinstance(orig_vals, BaseMaskedArray):
        assert result_mask is not None  # for mypy

        if interpolation in {"linear", "midpoint"} and not is_float_dtype(
            orig_vals
        ):
            exit(FloatingArray(vals, result_mask))
        else:
            # Item "ExtensionDtype" of "Union[ExtensionDtype, str,
            # dtype[Any], Type[object]]" has no attribute "numpy_dtype"
            # [union-attr]
            exit(type(orig_vals)(
                vals.astype(
                    inference.numpy_dtype  # type: ignore[union-attr]
                ),
                result_mask,
            ))

    elif not (
        is_integer_dtype(inference)
        and interpolation in {"linear", "midpoint"}
    ):
        assert isinstance(inference, np.dtype)  # for mypy
        exit(vals.astype(inference))

exit(vals)
