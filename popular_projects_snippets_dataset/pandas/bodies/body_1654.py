# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
arr = np.random.randint(-1 << 12, 1 << 12, (1 << 15, 5))
i = np.random.choice(len(arr), len(arr) * 4)
arr = np.vstack((arr, arr[i]))  # add some duplicate rows

i = np.random.permutation(len(arr))
arr = arr[i]  # shuffle rows

df = DataFrame(arr, columns=list("abcde"))
df["jim"], df["joe"] = np.random.randn(2, len(df)) * 10
gr = df.groupby(list("abcde"))

# verify this is testing what it is supposed to test!
assert is_int64_overflow_possible(gr.grouper.shape)

# manually compute groupings
jim, joe = defaultdict(list), defaultdict(list)
for key, a, b in zip(map(tuple, arr), df["jim"], df["joe"]):
    jim[key].append(a)
    joe[key].append(b)

assert len(gr) == len(jim)
mi = MultiIndex.from_tuples(jim.keys(), names=list("abcde"))

f = lambda a: np.fromiter(map(getattr(np, agg), a), dtype="f8")
arr = np.vstack((f(jim.values()), f(joe.values()))).T
res = DataFrame(arr, columns=["jim", "joe"], index=mi).sort_index()

tm.assert_frame_equal(getattr(gr, agg)(), res)
