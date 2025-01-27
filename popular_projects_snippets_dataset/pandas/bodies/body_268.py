# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
lhs = lhs < 0
rhs = rhs < 0

if parser == "python" and cmp_op in ["in", "not in"]:
    msg = "'(In|NotIn)' nodes are not implemented"

    with pytest.raises(NotImplementedError, match=msg):
        ex = f"lhs {cmp_op} rhs"
        pd.eval(ex, engine=engine, parser=parser)
    exit()

ex = f"lhs {cmp_op} rhs"
msg = "|".join(
    [
        r"only list-like( or dict-like)? objects are allowed to be "
        r"passed to (DataFrame\.)?isin\(\), you passed a "
        r"(\[|')bool(\]|')",
        "argument of type 'bool' is not iterable",
    ]
)
if cmp_op in ("in", "not in") and not is_list_like(rhs):
    with pytest.raises(TypeError, match=msg):
        pd.eval(
            ex,
            engine=engine,
            parser=parser,
            local_dict={"lhs": lhs, "rhs": rhs},
        )
else:
    expected = _eval_single_bin(lhs, cmp_op, rhs, engine)
    result = pd.eval(ex, engine=engine, parser=parser)
    tm.assert_equal(result, expected)
