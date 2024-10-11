# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
opname = all_numeric_reductions

ser = pd.Series(data)

should_work = True
if pa.types.is_temporal(pa_dtype) and opname in [
    "sum",
    "var",
    "skew",
    "kurt",
    "prod",
]:
    if pa.types.is_duration(pa_dtype) and opname in ["sum"]:
        # summing timedeltas is one case that *is* well-defined
        pass
    else:
        should_work = False
elif (
    pa.types.is_string(pa_dtype) or pa.types.is_binary(pa_dtype)
) and opname in [
    "sum",
    "mean",
    "median",
    "prod",
    "std",
    "sem",
    "var",
    "skew",
    "kurt",
]:
    should_work = False

if not should_work:
    # matching the non-pyarrow versions, these operations *should* not
    #  work for these dtypes
    msg = f"does not support reduction '{opname}'"
    with pytest.raises(TypeError, match=msg):
        getattr(ser, opname)(skipna=skipna)

    exit()

xfail_mark = pytest.mark.xfail(
    raises=TypeError,
    reason=(
        f"{all_numeric_reductions} is not implemented in "
        f"pyarrow={pa.__version__} for {pa_dtype}"
    ),
)
if all_numeric_reductions in {"skew", "kurt"}:
    request.node.add_marker(xfail_mark)
elif (
    all_numeric_reductions in {"median", "var", "std", "prod", "max", "min"}
    and pa_version_under6p0
):
    request.node.add_marker(xfail_mark)
elif all_numeric_reductions == "sem" and pa_version_under8p0:
    request.node.add_marker(xfail_mark)
elif (
    all_numeric_reductions in {"sum", "mean"}
    and skipna is False
    and pa_version_under6p0
    and (pa.types.is_integer(pa_dtype) or pa.types.is_floating(pa_dtype))
):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=AssertionError,
            reason=(
                f"{all_numeric_reductions} with skip_nulls={skipna} did not "
                f"return NA for {pa_dtype} with pyarrow={pa.__version__}"
            ),
        )
    )

elif all_numeric_reductions in [
    "mean",
    "median",
    "std",
    "sem",
] and pa.types.is_temporal(pa_dtype):
    request.node.add_marker(xfail_mark)
elif all_numeric_reductions in ["sum", "min", "max"] and pa.types.is_duration(
    pa_dtype
):
    request.node.add_marker(xfail_mark)
elif pa.types.is_boolean(pa_dtype) and all_numeric_reductions in {
    "sem",
    "std",
    "var",
    "median",
}:
    request.node.add_marker(xfail_mark)
super().test_reduce_series(data, all_numeric_reductions, skipna)
