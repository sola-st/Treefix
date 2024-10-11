# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Instantiates a new Stream object
        """
stream = Stream(
    stream_id=next(self._stream_id_generator),
    request=request,
    protocol=self,
    download_maxsize=getattr(spider, 'download_maxsize', self.metadata['default_download_maxsize']),
    download_warnsize=getattr(spider, 'download_warnsize', self.metadata['default_download_warnsize']),
)
self.streams[stream.stream_id] = stream
exit(stream)
