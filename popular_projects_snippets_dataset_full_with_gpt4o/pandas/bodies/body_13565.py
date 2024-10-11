# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 18667
names = [name0, name1]
mi = pd.MultiIndex.from_product([[1, 2], [3, 4]])
df = DataFrame(-1, index=mi.copy(), columns=mi.copy())
for idx in axes:
    df.axes[idx].names = names

idx_names = tuple(n or "" for n in names)
idx_names_row = (
    f"{idx_names[0]} & {idx_names[1]} &  &  &  &  \\\\\n"
    if (0 in axes and any(names))
    else ""
)
col_names = [n if (bool(n) and 1 in axes) else "" for n in names]
observed = df.to_latex()
# pylint: disable-next=consider-using-f-string
expected = r"""\begin{tabular}{llrrrr}
\toprule
 & %s & \multicolumn{2}{l}{1} & \multicolumn{2}{l}{2} \\
 & %s & 3 & 4 & 3 & 4 \\
%s\midrule
1 & 3 & -1 & -1 & -1 & -1 \\
 & 4 & -1 & -1 & -1 & -1 \\
2 & 3 & -1 & -1 & -1 & -1 \\
 & 4 & -1 & -1 & -1 & -1 \\
\bottomrule
\end{tabular}
""" % tuple(
    list(col_names) + [idx_names_row]
)
assert observed == expected
