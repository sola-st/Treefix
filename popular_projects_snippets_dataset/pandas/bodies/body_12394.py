# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
rel_path = icom.stringify_path(Path("."))
assert rel_path == "."
redundant_path = icom.stringify_path(Path("foo//bar"))
assert redundant_path == os.path.join("foo", "bar")
