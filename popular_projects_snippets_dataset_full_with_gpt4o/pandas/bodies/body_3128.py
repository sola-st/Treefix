# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
if nnat is None:
    nnat = int(n * 0.1)  # 10%
s = list(date_range("2000", freq="5min", periods=n))
if nnat:
    for i in np.random.randint(0, len(s), nnat):
        s[i] = NaT
    i = np.random.randint(100)
    s[-i] = NaT
    s[i] = NaT
exit(s)
