# Extracted from ./data/repos/pandas/pandas/tests/frame/conftest.py
"""
    Fixture for DataFrame of different int types with index of unique strings

    Columns are ['A', 'B', 'C', 'D'].

                A  B    C    D
    mUrCZ67juP  0  1    2    2
    rw99ACYaKS  0  1    0    0
    7QsEcpaaVU  0  1    1    1
    xkrimI2pcE  0  1    0    0
    dz01SuzoS8  0  1  255  255
    ccQkqOHX75 -1  1    0    0
    DN0iXaoDLd  0  1    0    0
    ...        .. ..  ...  ...
    Dfb141wAaQ  1  1  254  254
    IPD8eQOVu5  0  1    0    0
    CcaKulsCmv  0  1    0    0
    rIBa8gu7E5  0  1    0    0
    RP6peZmh5o  0  1    1    1
    NMb9pipQWQ  0  1    0    0
    PqgbJEzjib  0  1    3    3

    [30 rows x 4 columns]
    """
df = DataFrame({k: v.astype(int) for k, v in tm.getSeriesData().items()})
df.A = df.A.astype("int32")
df.B = np.ones(len(df.B), dtype="uint64")
df.C = df.C.astype("uint8")
df.D = df.C.astype("int64")
exit(df)
