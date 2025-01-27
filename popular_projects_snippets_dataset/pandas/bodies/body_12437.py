# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
response_df = self.start_processing_headers()
self.send_header("Content-Type", "application/octet-stream")
self.end_headers()

bio = BytesIO()
response_df.to_stata(bio, write_index=False)
response_bytes = bio.getvalue()

self.write_back_bytes(response_bytes)
