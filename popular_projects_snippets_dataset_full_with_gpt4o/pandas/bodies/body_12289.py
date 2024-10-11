# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py

# GH 4626, proper encoding handling
raw = read_stata(datapath("io", "data", "stata", "stata1_encoding.dta"))
encoded = read_stata(datapath("io", "data", "stata", "stata1_encoding.dta"))
result = encoded.kreis1849[0]

expected = raw.kreis1849[0]
assert result == expected
assert isinstance(result, str)

with tm.ensure_clean() as path:
    encoded.to_stata(path, write_index=False, version=version)
    reread_encoded = read_stata(path)
    tm.assert_frame_equal(encoded, reread_encoded)
