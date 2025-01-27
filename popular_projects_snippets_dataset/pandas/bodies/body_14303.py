# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py

path = tmp_path / setup_path

store = HDFStore(path, mode="a")
store["a"] = tm.makeTimeSeries()

msg = (
    r"Re-opening the file \[[\S]*\] with mode \[a\] will delete the "
    "current file!"
)
# invalid mode change
with pytest.raises(PossibleDataLossError, match=msg):
    store.open("w")

store.close()
assert not store.is_open

# truncation ok here
store.open("w")
assert store.is_open
assert len(store) == 0
store.close()
assert not store.is_open

store = HDFStore(path, mode="a")
store["a"] = tm.makeTimeSeries()

# reopen as read
store.open("r")
assert store.is_open
assert len(store) == 1
assert store._mode == "r"
store.close()
assert not store.is_open

# reopen as append
store.open("a")
assert store.is_open
assert len(store) == 1
assert store._mode == "a"
store.close()
assert not store.is_open

# reopen as append (again)
store.open("a")
assert store.is_open
assert len(store) == 1
assert store._mode == "a"
store.close()
assert not store.is_open
