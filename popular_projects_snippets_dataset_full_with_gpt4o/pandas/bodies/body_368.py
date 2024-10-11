# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
cannot_resolve = 42, 3.0
with pytest.raises(TypeError, match="Resolver of type .+"):
    pd.eval("1 + 2", resolvers=cannot_resolve, engine=engine, parser=parser)
