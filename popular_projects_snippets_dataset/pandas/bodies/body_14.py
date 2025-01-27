# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py

df = DataFrame({"A": range(5), "B": 5})

# nested renaming
msg = r"nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    getattr(df, method)({"A": {"foo": "min"}, "B": {"bar": "max"}})
