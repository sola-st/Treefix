from mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
client = Mock() # pragma: no cover
request = Mock(meta={'ftp_local_filename': 'example.txt'}) # pragma: no cover
filepath = '/path/to/file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
from l3.Runtime import _l_
self.client = client
_l_(8225)
protocol = ReceivedDataProtocol(request.meta.get("ftp_local_filename"))
_l_(8226)
aux = client.retrieveFile(filepath, protocol).addCallbacks(
    callback=self._build_response,
    callbackArgs=(request, protocol),
    errback=self._failed,
    errbackArgs=(request,),
)
_l_(8227)
exit(aux)
