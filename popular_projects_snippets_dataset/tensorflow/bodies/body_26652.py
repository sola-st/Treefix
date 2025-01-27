# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Blocks until the server has shut down.

    This is useful when starting a dedicated worker process.

    ```
    worker_server = tf.data.experimental.service.WorkerServer(
        port=5051, dispatcher_address="localhost:5050")
    worker_server.join()
    ```

    This method currently blocks forever.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        joining the server.
    """
self._server.join()
