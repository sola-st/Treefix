# Extracted from ./data/repos/pandas/pandas/tests/test_optional_dependency.py
name = "fakemodule"
module = types.ModuleType(name)
sys.modules[name] = module
monkeypatch.setitem(VERSIONS, name, "1.0.0")

with pytest.raises(ImportError, match="Can't determine .* fakemodule"):
    import_optional_dependency(name)
