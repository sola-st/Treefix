# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""
        Arguments:
            uri -- URI of the base url to which HTTP/2 Connection will be made.
                uri is used to verify that incoming client requests have correct
                base URL.
            settings -- Scrapy project settings
            conn_lost_deferred -- Deferred fires with the reason: Failure to notify
                that connection was lost
        """
self._conn_lost_deferred = conn_lost_deferred

config = H2Configuration(client_side=True, header_encoding='utf-8')
self.conn = H2Connection(config=config)

# ID of the next request stream
# Following the convention - 'Streams initiated by a client MUST
# use odd-numbered stream identifiers' (RFC 7540 - Section 5.1.1)
self._stream_id_generator = itertools.count(start=1, step=2)

# Streams are stored in a dictionary keyed off their stream IDs
self.streams: Dict[int, Stream] = {}

# If requests are received before connection is made we keep
# all requests in a pool and send them as the connection is made
self._pending_request_stream_pool: deque = deque()

# Save an instance of errors raised which lead to losing the connection
# We pass these instances to the streams ResponseFailed() failure
self._conn_lost_errors: List[BaseException] = []

# Some meta data of this connection
# initialized when connection is successfully made
self.metadata: Dict = {
    # Peer certificate instance
    'certificate': None,

    # Address of the server we are connected to which
    # is updated when HTTP/2 connection is  made successfully
    'ip_address': None,

    # URI of the peer HTTP/2 connection is made
    'uri': uri,

    # Both ip_address and uri are used by the Stream before
    # initiating the request to verify that the base address

    # Variables taken from Project Settings
    'default_download_maxsize': settings.getint('DOWNLOAD_MAXSIZE'),
    'default_download_warnsize': settings.getint('DOWNLOAD_WARNSIZE'),

    # Counter to keep track of opened streams. This counter
    # is used to make sure that not more than MAX_CONCURRENT_STREAMS
    # streams are opened which leads to ProtocolError
    # We use simple FIFO policy to handle pending requests
    'active_streams': 0,

    # Flag to keep track if settings were acknowledged by the remote
    # This ensures that we have established a HTTP/2 connection
    'settings_acknowledged': False,
}
