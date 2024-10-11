# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# gh 12666 - check no segfault
x17 = np.array([complex(i) for i in range(17)], dtype=object)

msg = "'[<>]' not supported between instances of .*"
with pytest.raises(TypeError, match=msg):
    algos.factorize(x17[::-1], sort=True)
