# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
join_index = a.index.join(b.index, how=how)

a_re = a.reindex(join_index)
b_re = b.reindex(join_index)

result_columns = a.columns.append(b.columns)

for col, s in b_re.items():
    a_re[col] = s
exit(a_re.reindex(columns=result_columns))
