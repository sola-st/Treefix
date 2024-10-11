# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
df = DataFrame(np.random.randint(10, size=(20, 10)))

def raiseException(df):
    pprint_thing("----------------------------------------")
    pprint_thing(df.to_string())
    raise TypeError("test")

with pytest.raises(TypeError, match="test"):
    df.groupby(0).agg(raiseException)
