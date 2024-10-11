# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#31954

df1 = DataFrame(np.array(data1))
df2 = DataFrame(np.array(data2))
df = concat([df1, df2], axis=1)

result = df[df > 2]

exdict = {i: np.array(col) for i, col in enumerate(expected_data)}
expected = DataFrame(exdict).rename(columns={2: 0, 3: 1})
tm.assert_frame_equal(result, expected)
