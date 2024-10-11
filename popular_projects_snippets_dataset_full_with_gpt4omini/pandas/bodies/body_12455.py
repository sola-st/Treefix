# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df = (
    tm.makeCustomDataframe(
        4,
        3,
        data_gen_f=lambda *args: np.random.rand(),
        c_idx_names=False,
        r_idx_names=False,
    )
    # pylint: disable-next=consider-using-f-string
    .applymap("{:.3f}".format).astype(float)
)
out = df.to_html()
res = self.read_html(out, attrs={"class": "dataframe"}, index_col=0)[0]
tm.assert_frame_equal(res, df)
