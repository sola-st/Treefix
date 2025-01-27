# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_allowlist.py
letters = np.array(list(ascii_lowercase))
N = 10
random_letters = letters.take(np.random.randint(0, 26, N))
df = DataFrame(
    {
        "floats": N / 10 * Series(np.random.random(N)),
        "letters": Series(random_letters),
    }
)
exit(df)
