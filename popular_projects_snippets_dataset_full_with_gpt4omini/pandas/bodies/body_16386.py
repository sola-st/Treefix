# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#44514
msg = "|".join(
    [
        "cannot safely cast non-equivalent object",
        r"int\(\) argument must be a string, a bytes-like object "
        "or a (real )?number",
        r"Cannot cast array data from dtype\('O'\) to dtype\('float64'\) "
        "according to the rule 'safe'",
        "object cannot be converted to a FloatingDtype",
        "'values' contains non-numeric NA",
    ]
)

for null in tm.NP_NAT_OBJECTS + [NaT]:
    with pytest.raises(TypeError, match=msg):
        func([null, 1.0, 3.0], dtype=any_numeric_ea_dtype)
