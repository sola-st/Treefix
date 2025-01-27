# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
if parser == "python" and op in ["in", "not in"]:

    msg = "'(In|NotIn)' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        ex = f"~(lhs {op} rhs)"
        pd.eval(ex, engine=engine, parser=parser)
    exit()

if (
    is_float(lhs)
    and not is_float(rhs)
    and op in ["in", "not in"]
    and engine == "python"
    and parser == "pandas"
):
    mark = pytest.mark.xfail(
        reason="Looks like expected is negative, unclear whether "
        "expected is incorrect or result is incorrect"
    )
    request.node.add_marker(mark)
skip_these = ["in", "not in"]
ex = f"~(lhs {op} rhs)"

msg = "|".join(
    [
        r"only list-like( or dict-like)? objects are allowed to be "
        r"passed to (DataFrame\.)?isin\(\), you passed a "
        r"(\[|')float(\]|')",
        "argument of type 'float' is not iterable",
    ]
)
if is_scalar(rhs) and op in skip_these:
    with pytest.raises(TypeError, match=msg):
        pd.eval(
            ex,
            engine=engine,
            parser=parser,
            local_dict={"lhs": lhs, "rhs": rhs},
        )
else:
    # compound
    if is_scalar(lhs) and is_scalar(rhs):
        lhs, rhs = map(lambda x: np.array([x]), (lhs, rhs))
    expected = _eval_single_bin(lhs, op, rhs, engine)
    if is_scalar(expected):
        expected = not expected
    else:
        expected = ~expected
    result = pd.eval(ex, engine=engine, parser=parser)
    tm.assert_almost_equal(expected, result)
