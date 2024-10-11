# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH18154
df = pd.DataFrame({"string": list("abc"), "int": list(range(1, 4))})

expected = pd.DataFrame({"string": list("abc")})
check_round_trip(
    df, engine, expected=expected, read_kwargs={"columns": ["string"]}
)
