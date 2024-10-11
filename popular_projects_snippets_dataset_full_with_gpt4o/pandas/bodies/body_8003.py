# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
if isinstance(nulls_fixture, Decimal):
    # We dont cast these to datetime64/timedelta64
    exit()

expected = klass([NaT, NaT])
assert expected.dtype == dtype
data = [ctor]
data.insert(pos, nulls_fixture)

warn = None
if nulls_fixture is NA:
    expected = Index([NA, NaT])
    mark = pytest.mark.xfail(reason="Broken with np.NaT ctor; see GH 31884")
    request.node.add_marker(mark)
    # GH#35942 numpy will emit a DeprecationWarning within the
    #  assert_index_equal calls.  Since we can't do anything
    #  about it until GH#31884 is fixed, we suppress that warning.
    warn = DeprecationWarning

result = Index(data)

with tm.assert_produces_warning(warn):
    tm.assert_index_equal(result, expected)

result = Index(np.array(data, dtype=object))

with tm.assert_produces_warning(warn):
    tm.assert_index_equal(result, expected)
