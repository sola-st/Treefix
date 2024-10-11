# Extracted from ./data/repos/pandas/pandas/tests/test_optional_dependency.py
name = "fakemodule"
module = types.ModuleType(name)
module.__version__ = "0.9.0"
sys.modules[name] = module
monkeypatch.setitem(VERSIONS, name, "1.0.0")

match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"
with pytest.raises(ImportError, match=match):
    import_optional_dependency("fakemodule")

# Test min_version parameter
result = import_optional_dependency("fakemodule", min_version="0.8")
assert result is module

with tm.assert_produces_warning(UserWarning):
    result = import_optional_dependency("fakemodule", errors="warn")
assert result is None

module.__version__ = "1.0.0"  # exact match is OK
result = import_optional_dependency("fakemodule")
assert result is module
