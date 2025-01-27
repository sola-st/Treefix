# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
with http.server.HTTPServer(("localhost", port), responder) as server:
    server.handle_request()
server.server_close()
