# Extracted from ./data/repos/pandas/pandas/tests/util/test_safe_import.py
mod_name = "hello123"

mod = types.ModuleType(mod_name)
mod.__version__ = "1.5"

if min_version is not None:
    monkeypatch.setitem(sys.modules, mod_name, mod)

result = td.safe_import(mod_name, min_version=min_version)
result = result if valid else not result
assert result
