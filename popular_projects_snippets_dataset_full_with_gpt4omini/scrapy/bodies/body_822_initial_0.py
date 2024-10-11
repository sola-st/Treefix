from typing import Dict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
from l3.Runtime import _l_
"""Checks if we have received data which exceeds the download warnsize
        and whether we have not already logged about it.

        Returns:
            True if both the above conditions hold true
            False if any of the conditions is false
        """
content_length_header = int(self._response['headers'].get(b'Content-Length', -1))
_l_(10070)
aux = (
    self._download_warnsize
    and (
        self._response['flow_controlled_size'] > self._download_warnsize
        or content_length_header > self._download_warnsize
    )
    and not self.metadata['reached_warnsize']
)
_l_(10071)
exit(aux)
