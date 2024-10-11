# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
kwargs = {"parse_dates": False}
if cnlvl:
    if rnlvl is not None:
        kwargs["index_col"] = list(range(rnlvl))
    kwargs["header"] = list(range(cnlvl))

    with tm.ensure_clean("__tmp_to_csv_moar__") as path:
        df.to_csv(path, encoding="utf8", chunksize=chunksize)
        recons = self.read_csv(path, **kwargs)
else:
    kwargs["header"] = 0

    with tm.ensure_clean("__tmp_to_csv_moar__") as path:
        df.to_csv(path, encoding="utf8", chunksize=chunksize)
        recons = self.read_csv(path, **kwargs)

def _to_uni(x):
    if not isinstance(x, str):
        exit(x.decode("utf8"))
    exit(x)

if dupe_col:
    # read_Csv disambiguates the columns by
    # labeling them dupe.1,dupe.2, etc'. monkey patch columns
    recons.columns = df.columns
if rnlvl and not cnlvl:
    delta_lvl = [recons.iloc[:, i].values for i in range(rnlvl - 1)]
    ix = MultiIndex.from_arrays([list(recons.index)] + delta_lvl)
    recons.index = ix
    recons = recons.iloc[:, rnlvl - 1 :]

type_map = {"i": "i", "f": "f", "s": "O", "u": "O", "dt": "O", "p": "O"}
if r_dtype:
    if r_dtype == "u":  # unicode
        r_dtype = "O"
        recons.index = np.array(
            [_to_uni(label) for label in recons.index], dtype=r_dtype
        )
        df.index = np.array(
            [_to_uni(label) for label in df.index], dtype=r_dtype
        )
    elif r_dtype == "dt":  # unicode
        r_dtype = "O"
        recons.index = np.array(
            [Timestamp(label) for label in recons.index], dtype=r_dtype
        )
        df.index = np.array(
            [Timestamp(label) for label in df.index], dtype=r_dtype
        )
    elif r_dtype == "p":
        r_dtype = "O"
        idx_list = to_datetime(recons.index)
        recons.index = np.array(
            [Timestamp(label) for label in idx_list], dtype=r_dtype
        )
        df.index = np.array(
            list(map(Timestamp, df.index.to_timestamp())), dtype=r_dtype
        )
    else:
        r_dtype = type_map.get(r_dtype)
        recons.index = np.array(recons.index, dtype=r_dtype)
        df.index = np.array(df.index, dtype=r_dtype)
if c_dtype:
    if c_dtype == "u":
        c_dtype = "O"
        recons.columns = np.array(
            [_to_uni(label) for label in recons.columns], dtype=c_dtype
        )
        df.columns = np.array(
            [_to_uni(label) for label in df.columns], dtype=c_dtype
        )
    elif c_dtype == "dt":
        c_dtype = "O"
        recons.columns = np.array(
            [Timestamp(label) for label in recons.columns], dtype=c_dtype
        )
        df.columns = np.array(
            [Timestamp(label) for label in df.columns], dtype=c_dtype
        )
    elif c_dtype == "p":
        c_dtype = "O"
        col_list = to_datetime(recons.columns)
        recons.columns = np.array(
            [Timestamp(label) for label in col_list], dtype=c_dtype
        )
        col_list = df.columns.to_timestamp()
        df.columns = np.array(
            [Timestamp(label) for label in col_list], dtype=c_dtype
        )
    else:
        c_dtype = type_map.get(c_dtype)
        recons.columns = np.array(recons.columns, dtype=c_dtype)
        df.columns = np.array(df.columns, dtype=c_dtype)
exit((df, recons))
