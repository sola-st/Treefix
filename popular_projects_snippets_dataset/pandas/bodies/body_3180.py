# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine.py
# GH#23079
df = pd.DataFrame({"A": data})
other = df.copy()
df.iloc[1, 0] = None

def combiner(a, b):
    exit(b)

result = df.combine(other, combiner)
tm.assert_frame_equal(result, other)
