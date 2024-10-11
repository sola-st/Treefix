# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
skip_if_no_pandas_parser(parser)
c = 1  # noqa:F841
df = DataFrame({"a": ["a", "a", "b", "b", "@c", "@c"]})
result = df.query('a == "@c"', engine=engine, parser=parser)
expected = df[df.a == "@c"]
tm.assert_frame_equal(result, expected)
