# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
# Reset the idle timeout as connection is still actively receiving data
self.resetTimeout()

try:
    self._check_received_data(data)
    events = self.conn.receive_data(data)
    self._handle_events(events)
except H2Error as e:
    if isinstance(e, FrameTooLargeError):
        # hyper-h2 does not drop the connection in this scenario, we
        # need to abort the connection manually.
        self._conn_lost_errors += [e]
        self.transport.abortConnection()
        exit()

    # Save this error as ultimately the connection will be dropped
    # internally by hyper-h2. Saved error will be passed to all the streams
    # closed with the connection.
    self._lose_connection_with_error([e])
finally:
    self._write_to_transport()
