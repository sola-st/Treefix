# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
# This will become relevant for test_constructor_dict_timedelta64_index
#  once Timedelta constructor preserves reso when passed a
#  np.timedelta64 object
td = Timedelta(days=1)

mapping1 = {td: 1}
mapping2 = {td.as_unit("s"): 1}

oindex = Index([td * n for n in range(3)])._values.astype(object)

expected = lib.fast_multiget(mapping1, oindex)
result = lib.fast_multiget(mapping2, oindex)
tm.assert_numpy_array_equal(result, expected)

# case that can't be cast to td64ns
td = Timedelta(np.timedelta64(400, "Y"))
assert hash(td) == hash(td.as_unit("ms"))
assert hash(td) == hash(td.as_unit("us"))
mapping1 = {td: 1}
mapping2 = {td.as_unit("ms"): 1}

oindex = Index([td * n for n in range(3)])._values.astype(object)

expected = lib.fast_multiget(mapping1, oindex)
result = lib.fast_multiget(mapping2, oindex)
tm.assert_numpy_array_equal(result, expected)
