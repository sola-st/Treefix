# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
np.random.seed(0)
# Series of ints
s = Series(np.random.randint(0, 100, 1000))
grouper = s.apply(lambda x: np.round(x, -1))
grouped = s.groupby(grouper)
f = lambda x: x.mean() > 10

old_way = s[grouped.transform(f).astype("bool")]
new_way = grouped.filter(f)
tm.assert_series_equal(new_way.sort_values(), old_way.sort_values())

# Series of floats
s = 100 * Series(np.random.random(1000))
grouper = s.apply(lambda x: np.round(x, -1))
grouped = s.groupby(grouper)
f = lambda x: x.mean() > 10
old_way = s[grouped.transform(f).astype("bool")]
new_way = grouped.filter(f)
tm.assert_series_equal(new_way.sort_values(), old_way.sort_values())

# Set up DataFrame of ints, floats, strings.
letters = np.array(list(ascii_lowercase))
N = 1000
random_letters = letters.take(np.random.randint(0, 26, N))
df = DataFrame(
    {
        "ints": Series(np.random.randint(0, 100, N)),
        "floats": N / 10 * Series(np.random.random(N)),
        "letters": Series(random_letters),
    }
)

# Group by ints; filter on floats.
grouped = df.groupby("ints")
old_way = df[grouped.floats.transform(lambda x: x.mean() > N / 20).astype("bool")]
new_way = grouped.filter(lambda x: x["floats"].mean() > N / 20)
tm.assert_frame_equal(new_way, old_way)

# Group by floats (rounded); filter on strings.
grouper = df.floats.apply(lambda x: np.round(x, -1))
grouped = df.groupby(grouper)
old_way = df[grouped.letters.transform(lambda x: len(x) < N / 10).astype("bool")]
new_way = grouped.filter(lambda x: len(x.letters) < N / 10)
tm.assert_frame_equal(new_way, old_way)

# Group by strings; filter on ints.
grouped = df.groupby("letters")
old_way = df[grouped.ints.transform(lambda x: x.mean() > N / 20).astype("bool")]
new_way = grouped.filter(lambda x: x["ints"].mean() > N / 20)
tm.assert_frame_equal(new_way, old_way)
