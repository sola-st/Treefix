# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# ignore LocalPath: it creates strange paths: /absolute/~/sometest
with tempfile.TemporaryDirectory(dir=Path.home()) as tmp:
    filename = path_type("~/" + Path(tmp).name + "/sometest")
    with icom.get_handle(filename, "w") as handles:
        assert Path(handles.handle.name).is_absolute()
        assert os.path.expanduser(filename) == handles.handle.name
