# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
response_df = pd.DataFrame(self.headers.items())
self.send_response(200)
self.send_header("Content-Type", "text/csv")
self.end_headers()
response_bytes = response_df.to_csv(index=False).encode("utf-8")
self.wfile.write(response_bytes)
