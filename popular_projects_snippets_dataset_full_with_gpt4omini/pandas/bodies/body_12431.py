# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
response_df = self.start_processing_headers()
self.send_header("Content-Type", "text/csv")
self.send_header("Content-Encoding", "gzip")
self.end_headers()

response_bytes = response_df.to_csv(index=False).encode("utf-8")
response_bytes = self.gzip_bytes(response_bytes)

self.write_back_bytes(response_bytes)
