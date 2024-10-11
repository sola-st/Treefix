# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
kwargs = build_kwargs(sep, excel)
df.to_clipboard(**kwargs)
assert mock_clipboard[request.node.name] == df.to_csv(sep="\t")
