# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-1978, gh-1979
cut_file = datapath(os.path.join("reshape", "data", "cut_data.csv"))
arr = np.loadtxt(cut_file)
result = qcut(arr, 20)

starts = []
ends = []

for lev in np.unique(result):
    s = lev.left
    e = lev.right
    assert s != e

    starts.append(float(s))
    ends.append(float(e))

for (sp, sn), (ep, en) in zip(
    zip(starts[:-1], starts[1:]), zip(ends[:-1], ends[1:])
):
    assert sp < sn
    assert ep < en
    assert ep <= sn
