# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
response_df = self.start_processing_headers()
self.send_header("Content-Type", "application/octet-stream")
self.end_headers()

# the fastparquet engine doesn't like to write to a buffer
# it can do it via the open_with function being set appropriately
# however it automatically calls the close method and wipes the buffer
# so just overwrite that attribute on this instance to not do that

# protected by an importorskip in the respective test
import fsspec

response_df.to_parquet(
    "memory://fastparquet_user_agent.parquet",
    index=False,
    engine="fastparquet",
    compression=None,
)
with fsspec.open("memory://fastparquet_user_agent.parquet", "rb") as f:
    response_bytes = f.read()

self.write_back_bytes(response_bytes)
