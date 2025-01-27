# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
import scipy.stats  # noqa:F401
from scipy.stats import rankdata

xs = np.random.randint(0, 21, (100, 26))
xs = (xs - 10.0) / 10.0
cols = [chr(ord("z") - i) for i in range(xs.shape[1])]

for vals in [xs, xs + 1e6, xs * 1e-6]:
    df = DataFrame(vals, columns=cols)

    for ax in [0, 1]:
        for m in ["average", "min", "max", "first", "dense"]:
            result = df.rank(axis=ax, method=m)
            sprank = np.apply_along_axis(
                rankdata, ax, vals, m if m != "first" else "ordinal"
            )
            sprank = sprank.astype(np.float64)
            expected = DataFrame(sprank, columns=cols).astype("float64")
            tm.assert_frame_equal(result, expected)
