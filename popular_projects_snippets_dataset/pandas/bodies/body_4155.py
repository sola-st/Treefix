# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# GH 34966
df = DataFrame(np.random.randn(10, 2), columns=list("ab"))
dict1 = {"c": 2}

# Both input and default index/column resolvers should be usable
result = df.eval("a + b * c", resolvers=[dict1])

expected = df["a"] + df["b"] * dict1["c"]
tm.assert_series_equal(result, expected)
