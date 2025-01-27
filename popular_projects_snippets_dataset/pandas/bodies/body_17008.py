# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH 7864
# make sure ordering is preserved
df = DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": list("abbaae")})
df["grade"] = Categorical(df["raw_grade"])
df["grade"].cat.set_categories(["e", "a", "b"])

df1 = df[0:3]
df2 = df[3:]

tm.assert_index_equal(df["grade"].cat.categories, df1["grade"].cat.categories)
tm.assert_index_equal(df["grade"].cat.categories, df2["grade"].cat.categories)

dfx = pd.concat([df1, df2])
tm.assert_index_equal(df["grade"].cat.categories, dfx["grade"].cat.categories)

dfa = df1._append(df2)
tm.assert_index_equal(df["grade"].cat.categories, dfa["grade"].cat.categories)
