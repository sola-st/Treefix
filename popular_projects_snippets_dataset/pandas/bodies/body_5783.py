# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = next(data_repeated(1)).dtype.pyarrow_dtype
if pa.types.is_duration(pa_dtype):
    # TODO: this fails on the scalar addition constructing 'expected'
    #  but not in the actual 'combine' call, so may be salvage-able
    mark = pytest.mark.xfail(
        raises=TypeError,
        reason=f"{pa_dtype} cannot be added to {pa_dtype}",
    )
    request.node.add_marker(mark)
    super().test_combine_add(data_repeated)

elif pa.types.is_temporal(pa_dtype):
    # analogous to datetime64, these cannot be added
    orig_data1, orig_data2 = data_repeated(2)
    s1 = pd.Series(orig_data1)
    s2 = pd.Series(orig_data2)
    with pytest.raises(TypeError):
        s1.combine(s2, lambda x1, x2: x1 + x2)

else:
    super().test_combine_add(data_repeated)
