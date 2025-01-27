# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
from l3.Runtime import _l_
df = DataFrame(
    vals,
    index=pd.Index(
        (pd.Period(f"2022Q{q}") for q in range(1, 5)), name=index_nm
    ),
)
_l_(15494)
out = df.to_json(orient="table")
_l_(15495)
result = pd.read_json(out, orient="table")
_l_(15496)
tm.assert_frame_equal(df, result)
_l_(15497)
