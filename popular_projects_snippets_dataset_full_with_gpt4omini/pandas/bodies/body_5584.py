# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# gh 19727 - check warning is raised for deprecated keyword, order.
# Test not valid once order keyword is removed.
data = np.array([2**63, 1, 2**63], dtype=np.uint64)
with pytest.raises(TypeError, match="got an unexpected keyword"):
    algos.factorize(data, order=True)
with tm.assert_produces_warning(False):
    algos.factorize(data)
