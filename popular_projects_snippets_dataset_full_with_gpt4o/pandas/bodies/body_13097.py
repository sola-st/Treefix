# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-7074
with BytesIO() as bio:
    df = DataFrame(np.random.randn(10, 2))

    # Pass engine explicitly, as there is no file path to infer from.
    with ExcelWriter(bio, engine=engine) as writer:
        df.to_excel(writer)

    bio.seek(0)
    reread_df = pd.read_excel(bio, index_col=0)
    tm.assert_frame_equal(df, reread_df)
