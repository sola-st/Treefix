# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
response_df = self.start_processing_headers()
self.send_header("Content-Type", "application/octet-stream")
self.end_headers()

response_bytes = response_df.to_parquet(index=False, engine="pyarrow")

self.write_back_bytes(response_bytes)
