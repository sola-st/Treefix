# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
f1 = StringIO("a,1.0\nb,2.0")
df = self.read_csv(f1, header=None)
newdf = DataFrame({"t": df[df.columns[0]]})

with tm.ensure_clean() as path:
    newdf.to_csv(path)

    recons = read_csv(path, index_col=0)
    # don't check_names as t != 1
    tm.assert_frame_equal(recons, newdf, check_names=False)
