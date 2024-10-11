# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df = DataFrame({"a": [1 + 1j, 2j]})
msg = "Complex datatypes not supported"
with pytest.raises(ValueError, match=msg):
    assert df.to_sql("test_complex", self.conn) is None
