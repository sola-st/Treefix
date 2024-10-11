# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
df = DataFrame(np.random.randn(10, 4)).astype(type)

msg = "Limit must be an integer"
with pytest.raises(ValueError, match=msg):
    df.fillna(0, limit=0.5)
