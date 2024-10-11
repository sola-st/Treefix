# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 29854
with tm.ensure_clean(ext) as filename:

    df1 = DataFrame({"A": np.linspace(1, 10, 10)})
    df2 = DataFrame({"B": np.linspace(1, 20, 10)})
    df = pd.concat([df1, df2], axis=1)
    styled = df.style.applymap(
        lambda val: f"color: {'red' if val < 0 else 'black'}"
    ).highlight_max()

    styled.to_excel(filename, engine="openpyxl")
