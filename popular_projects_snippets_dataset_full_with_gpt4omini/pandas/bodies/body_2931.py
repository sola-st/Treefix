# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_period.py
dr = date_range("1/1/2000", "1/1/2001")
df = DataFrame(np.random.randn(len(dr), 5), index=dr)
df["mix"] = "a"

msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    df.to_period(axis=2)
