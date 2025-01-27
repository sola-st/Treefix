# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 46718
long_json_path = f'{"a" * 1000}.json{compression}'
with pytest.raises(
    FileNotFoundError, match=f"File {long_json_path} does not exist"
):
    # path too long for Windows is handled in file_exists() but raises in
    # _get_data_from_filepath()
    read_json(long_json_path)
