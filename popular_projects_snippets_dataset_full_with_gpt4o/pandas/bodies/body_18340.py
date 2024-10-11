# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# Variants of `one` for #19012, deprecated GH#22535
rng = timedelta_range("1 days 09:00:00", freq="H", periods=10)
tdarr = tm.box_expected(rng, box_with_array)

msg = "Addition/subtraction of integers"
assert_invalid_addsub_type(tdarr, one, msg)

# TODO: get inplace ops into assert_invalid_addsub_type
with pytest.raises(TypeError, match=msg):
    tdarr += one
with pytest.raises(TypeError, match=msg):
    tdarr -= one
