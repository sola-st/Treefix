# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
"""Flow control window size was changed.
        Send data that earlier could not be sent as we were
        blocked behind the flow control.
        """
if (
    self.metadata['remaining_content_length']
    and not self.metadata['stream_closed_server']
    and self.metadata['request_sent']
):
    self.send_data()
