# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
# GH#24569
arr = np.array([pd.Timestamp("2000"), pd.Timestamp("2000", tz="CET")])

msg = (
    "Cannot mix tz-aware with tz-naive values|"
    "Tz-aware datetime.datetime cannot be converted "
    "to datetime64 unless utc=True"
)

for obj in [arr, arr[::-1]]:
    # check that we raise regardless of whether naive is found
    #  before aware or vice-versa
    with pytest.raises(ValueError, match=msg):
        meth(obj)
