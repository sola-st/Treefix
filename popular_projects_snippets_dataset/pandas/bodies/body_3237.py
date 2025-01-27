# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
df = df_main_dtypes
col = columns[1]
error_msg = (
    f"Column '{col}' has dtype {df[col].dtype}, "
    f"cannot use method '{nselect_method}' with this dtype"
)
# escape some characters that may be in the repr
error_msg = (
    error_msg.replace("(", "\\(")
    .replace(")", "\\)")
    .replace("[", "\\[")
    .replace("]", "\\]")
)
with pytest.raises(TypeError, match=error_msg):
    getattr(df, nselect_method)(2, columns)
