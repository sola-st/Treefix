# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
dti = pd.date_range("2000-01-03", "2000-01-07")
# freq doesn't roundtrip
dti = DatetimeIndex(np.asarray(dti), freq=None)
df = DataFrame(
    [
        [1.56808523, 0.65727391, 1.81021139, -0.17251653],
        [-0.2550111, -0.08072427, -0.03202878, -0.17581665],
        [1.51493992, 0.11805825, 1.629455, -1.31506612],
        [-0.02765498, 0.44679743, 0.33192641, -0.27885413],
        [0.05951614, -2.69652057, 1.28163262, 0.34703478],
    ],
    columns=["A", "B", "C", "D"],
    index=dti,
)
df["date"] = Timestamp("19920106 18:21:32.12")
df.iloc[3, df.columns.get_loc("date")] = Timestamp("20130101")
df["modified"] = df["date"]
df.iloc[1, df.columns.get_loc("modified")] = pd.NaT

dirpath = datapath("io", "json", "data")
v12_json = os.path.join(dirpath, "tsframe_v012.json")
df_unser = read_json(v12_json)
tm.assert_frame_equal(df, df_unser)

df_iso = df.drop(["modified"], axis=1)
v12_iso_json = os.path.join(dirpath, "tsframe_iso_v012.json")
df_unser_iso = read_json(v12_iso_json)
tm.assert_frame_equal(df_iso, df_unser_iso)
