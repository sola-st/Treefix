# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
ex = "lhs // rhs"

if engine == "python":
    res = pd.eval(ex, engine=engine, parser=parser)
    expected = lhs // rhs
    tm.assert_equal(res, expected)
else:
    msg = (
        r"unsupported operand type\(s\) for //: 'VariableNode' and "
        "'VariableNode'"
    )
    with pytest.raises(TypeError, match=msg):
        pd.eval(
            ex,
            local_dict={"lhs": lhs, "rhs": rhs},
            engine=engine,
            parser=parser,
        )
