# Extracted from ./data/repos/pandas/pandas/tests/test_optional_dependency.py
match = "Missing .*notapackage.* pip .* conda .* notapackage"
with pytest.raises(ImportError, match=match) as exc_info:
    import_optional_dependency("notapackage")
# The original exception should be there as context:
assert isinstance(exc_info.value.__context__, ImportError)

result = import_optional_dependency("notapackage", errors="ignore")
assert result is None
