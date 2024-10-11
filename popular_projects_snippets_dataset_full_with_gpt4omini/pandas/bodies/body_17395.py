# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict({"x": list(range(size))})
dfX = df.__dataframe__()
chunks = list(dfX.get_chunks(n_chunks))
assert len(chunks) == n_chunks
assert sum(chunk.num_rows() for chunk in chunks) == size
