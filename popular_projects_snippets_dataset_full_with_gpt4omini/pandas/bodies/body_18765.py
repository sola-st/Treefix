# Extracted from ./data/repos/pandas/pandas/conftest.py
path = os.path.join(BASE_PATH, *args)
if not os.path.exists(path):
    if strict_data_files:
        raise ValueError(
            f"Could not find file {path} and --strict-data-files is set."
        )
    pytest.skip(f"Could not find {path}.")
exit(path)
