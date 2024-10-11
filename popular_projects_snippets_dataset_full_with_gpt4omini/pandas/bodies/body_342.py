# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
if parser != "python":
    res = pd.eval("1 in [1, 2]", engine=engine, parser=parser)
    assert res

    res = pd.eval("2 in (1, 2)", engine=engine, parser=parser)
    assert res

    res = pd.eval("3 in (1, 2)", engine=engine, parser=parser)
    assert not res

    res = pd.eval("3 not in (1, 2)", engine=engine, parser=parser)
    assert res

    res = pd.eval("[3] not in (1, 2)", engine=engine, parser=parser)
    assert res

    res = pd.eval("[3] in ([3], 2)", engine=engine, parser=parser)
    assert res

    res = pd.eval("[[3]] in [[[3]], 2]", engine=engine, parser=parser)
    assert res

    res = pd.eval("(3,) in [(3,), 2]", engine=engine, parser=parser)
    assert res

    res = pd.eval("(3,) not in [(3,), 2]", engine=engine, parser=parser)
    assert not res

    res = pd.eval("[(3,)] in [[(3,)], 2]", engine=engine, parser=parser)
    assert res
else:
    msg = "'In' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("1 in [1, 2]", engine=engine, parser=parser)
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("2 in (1, 2)", engine=engine, parser=parser)
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("3 in (1, 2)", engine=engine, parser=parser)
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("[(3,)] in (1, 2, [(3,)])", engine=engine, parser=parser)
    msg = "'NotIn' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("3 not in (1, 2)", engine=engine, parser=parser)
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval("[3] not in (1, 2, [[3]])", engine=engine, parser=parser)
