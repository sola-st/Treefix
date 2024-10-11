# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
if event.stream_id != 0:
    self.streams[event.stream_id].receive_window_update()
else:
    # Send leftover data for all the streams
    for stream in self.streams.values():
        stream.receive_window_update()
