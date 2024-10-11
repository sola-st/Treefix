# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(raises=TypeError, reason="GH 47534")
    )
elif pa.types.is_timestamp(pa_dtype) and pa_dtype.tz is not None:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason=f"Parameterized types with tz={pa_dtype.tz} not supported.",
        )
    )
elif pa.types.is_timestamp(pa_dtype) and pa_dtype.unit in ("us", "ns"):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=ValueError,
            reason="https://github.com/pandas-dev/pandas/issues/49767",
        )
    )
elif pa.types.is_binary(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(reason="CSV parsers don't correctly handle binary")
    )
df = pd.DataFrame({"with_dtype": pd.Series(data, dtype=str(data.dtype))})
csv_output = df.to_csv(index=False, na_rep=np.nan)
if pa.types.is_binary(pa_dtype):
    csv_output = BytesIO(csv_output)
else:
    csv_output = StringIO(csv_output)
result = pd.read_csv(
    csv_output, dtype={"with_dtype": str(data.dtype)}, engine=engine
)
expected = df
self.assert_frame_equal(result, expected)
