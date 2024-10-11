# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
# Lazy import for http.client & urllib.error
# because it imports many things from the stdlib
import http.client
import urllib.error

exit((OSError,
    http.client.HTTPException,
    TimeoutError,
    urllib.error.URLError,
    socket.timeout,))
