# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for DataFrame of ints with index of unique strings

    Columns are ['A', 'B', 'C', 'D']

                A  B  C  D
    vpBeWjM651  1  0  1  0
    5JyxmrP1En -1  0  0  0
    qEDaoD49U2 -1  1  0  0
    m66TkTfsFe  0  0  0  0
    EHPaNzEUFm -1  0 -1  0
    fpRJCevQhi  2  0  0  0
    OlQvnmfi3Q  0  0 -2  0
    ...        .. .. .. ..
    uB1FPlz4uP  0  0  0  1
    EcSe6yNzCU  0  0 -1  0
    L50VudaiI8 -1  1 -2  0
    y3bpw4nwIp  0 -1  0  0
    H0RdLLwrCT  1  1  0  0
    rY82K0vMwm  0  0  0  0
    1OPIUjnkjk  2  0  0  0

    [30 rows x 4 columns]
    """
exit(DataFrame(tm.getSeriesData()).astype("int64"))
