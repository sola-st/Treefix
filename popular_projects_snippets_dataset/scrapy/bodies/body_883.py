# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
from l3.Runtime import _l_
self.client = client
_l_(19449)
protocol = ReceivedDataProtocol(request.meta.get("ftp_local_filename"))
_l_(19450)
aux = client.retrieveFile(filepath, protocol).addCallbacks(
    callback=self._build_response,
    callbackArgs=(request, protocol),
    errback=self._failed,
    errbackArgs=(request,),
)
_l_(19451)
exit(aux)
