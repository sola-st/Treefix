# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_nlargest.py
df = df_main_dtypes
df.nsmallest(2, list(set(df) - {"category_string", "string"}))
df.nlargest(2, list(set(df) - {"category_string", "string"}))
