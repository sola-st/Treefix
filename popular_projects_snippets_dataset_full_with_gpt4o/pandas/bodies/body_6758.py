# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
item = data[0]
idx_item = IntervalIndex([item])

# start
expected = idx_item.append(data)
result = data.insert(0, item)
tm.assert_index_equal(result, expected)

# end
expected = data.append(idx_item)
result = data.insert(len(data), item)
tm.assert_index_equal(result, expected)

# mid
expected = data[:3].append(idx_item).append(data[3:])
result = data.insert(3, item)
tm.assert_index_equal(result, expected)

# invalid type
res = data.insert(1, "foo")
expected = data.astype(object).insert(1, "foo")
tm.assert_index_equal(res, expected)

msg = "can only insert Interval objects and NA into an IntervalArray"
with pytest.raises(TypeError, match=msg):
    data._data.insert(1, "foo")

# invalid closed
msg = "'value.closed' is 'left', expected 'right'."
for closed in {"left", "right", "both", "neither"} - {item.closed}:
    msg = f"'value.closed' is '{closed}', expected '{item.closed}'."
    bad_item = Interval(item.left, item.right, closed=closed)
    res = data.insert(1, bad_item)
    expected = data.astype(object).insert(1, bad_item)
    tm.assert_index_equal(res, expected)
    with pytest.raises(ValueError, match=msg):
        data._data.insert(1, bad_item)

        # GH 18295 (test missing)
na_idx = IntervalIndex([np.nan], closed=data.closed)
for na in [np.nan, None, pd.NA]:
    expected = data[:1].append(na_idx).append(data[1:])
    result = data.insert(1, na)
    tm.assert_index_equal(result, expected)

if data.left.dtype.kind not in ["m", "M"]:
    # trying to insert pd.NaT into a numeric-dtyped Index should cast
    expected = data.astype(object).insert(1, pd.NaT)

    msg = "can only insert Interval objects and NA into an IntervalArray"
    with pytest.raises(TypeError, match=msg):
        data._data.insert(1, pd.NaT)

result = data.insert(1, pd.NaT)
tm.assert_index_equal(result, expected)
