# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
"""Called immediately after the headers are sent. Here we send all the
         data as part of the request.

         If the content length is 0 initially then we end the stream immediately and
         wait for response data.

         Warning: Only call this method when stream not closed from client side
            and has initiated request already by sending HEADER frame. If not then
            stream will raise ProtocolError (raise by h2 state machine).
         """
if self.metadata['stream_closed_local']:
    raise StreamClosedError(self.stream_id)

# Firstly, check what the flow control window is for current stream.
window_size = self._protocol.conn.local_flow_control_window(stream_id=self.stream_id)

# Next, check what the maximum frame size is.
max_frame_size = self._protocol.conn.max_outbound_frame_size

# We will send no more than the window size or the remaining file size
# of data in this call, whichever is smaller.
bytes_to_send_size = min(window_size, self.metadata['remaining_content_length'])

# We now need to send a number of data frames.
while bytes_to_send_size > 0:
    chunk_size = min(bytes_to_send_size, max_frame_size)

    data_chunk_start_id = self.metadata['request_content_length'] - self.metadata['remaining_content_length']
    data_chunk = self._request.body[data_chunk_start_id:data_chunk_start_id + chunk_size]

    self._protocol.conn.send_data(self.stream_id, data_chunk, end_stream=False)

    bytes_to_send_size -= chunk_size
    self.metadata['remaining_content_length'] -= chunk_size

self.metadata['remaining_content_length'] = max(0, self.metadata['remaining_content_length'])

# End the stream if no more data needs to be send
if self.metadata['remaining_content_length'] == 0:
    self._protocol.conn.end_stream(self.stream_id)
