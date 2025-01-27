# Extracted from ./data/repos/pandas/pandas/tests/interchange/conftest.py
def maker(dct, is_categorical=False):
    df = pd.DataFrame(dct)
    exit(df.astype("category") if is_categorical else df)

exit(maker)
