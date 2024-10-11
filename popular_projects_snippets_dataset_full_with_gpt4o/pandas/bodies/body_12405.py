# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
pytest.importorskip(module)

dummy_frame = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})

path = os.path.join(HERE, "data", "missing_folder", "does_not_exist." + fn_ext)

with pytest.raises(
    error_class,
    match=r"Cannot save file into a non-existent directory: .*missing_folder",
):
    method(dummy_frame, path)
