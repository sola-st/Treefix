# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3))
if parser == "python":
    msg = "'BoolOp' nodes are not implemented"
    if "not" in expr:
        msg = "'Not' nodes are not implemented"

    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(
            expr,
            local_dict={"df": df},
            parser=parser,
            engine=engine,
        )
else:
    # smoke-test, should not raise
    pd.eval(
        expr,
        local_dict={"df": df},
        parser=parser,
        engine=engine,
    )
