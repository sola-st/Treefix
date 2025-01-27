# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 20647
df = DataFrame()
with pytest.raises(TypeError, match=".* got an unexpected keyword"):
    df.expanding(center=True)
