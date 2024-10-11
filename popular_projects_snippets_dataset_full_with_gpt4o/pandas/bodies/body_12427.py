# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
"""
        shared logic at the start of a GET request
        """
self.send_response(200)
self.requested_from_user_agent = self.headers["User-Agent"]
response_df = pd.DataFrame(
    {
        "header": [self.requested_from_user_agent],
    }
)
exit(response_df)
