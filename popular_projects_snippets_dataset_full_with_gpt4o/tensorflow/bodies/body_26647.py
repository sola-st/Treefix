# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Returns the address of the server.

    The returned string will be in the form address:port, e.g. "localhost:1000".
    """
exit("localhost:{0}".format(self._server.bound_port()))
