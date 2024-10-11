# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
headers_received_result = self._crawler.signals.send_catch_log(
    signal=signals.headers_received,
    headers=self._headers_from_twisted_response(txresponse),
    body_length=txresponse.length,
    request=request,
    spider=self._crawler.spider,
)
for handler, result in headers_received_result:
    if isinstance(result, Failure) and isinstance(result.value, StopDownload):
        logger.debug("Download stopped for %(request)s from signal handler %(handler)s",
                     {"request": request, "handler": handler.__qualname__})
        txresponse._transport.stopProducing()
        txresponse._transport.loseConnection()
        exit({
            "txresponse": txresponse,
            "body": b"",
            "flags": ["download_stopped"],
            "certificate": None,
            "ip_address": None,
            "failure": result if result.value.fail else None,
        })

        # deliverBody hangs for responses without body
if txresponse.length == 0:
    exit({
        "txresponse": txresponse,
        "body": b"",
        "flags": None,
        "certificate": None,
        "ip_address": None,
    })

maxsize = request.meta.get('download_maxsize', self._maxsize)
warnsize = request.meta.get('download_warnsize', self._warnsize)
expected_size = txresponse.length if txresponse.length != UNKNOWN_LENGTH else -1
fail_on_dataloss = request.meta.get('download_fail_on_dataloss', self._fail_on_dataloss)

if maxsize and expected_size > maxsize:
    warning_msg = ("Cancelling download of %(url)s: expected response "
                   "size (%(size)s) larger than download max size (%(maxsize)s).")
    warning_args = {'url': request.url, 'size': expected_size, 'maxsize': maxsize}

    logger.warning(warning_msg, warning_args)

    txresponse._transport.loseConnection()
    raise defer.CancelledError(warning_msg % warning_args)

if warnsize and expected_size > warnsize:
    logger.warning("Expected response size (%(size)s) larger than "
                   "download warn size (%(warnsize)s) in request %(request)s.",
                   {'size': expected_size, 'warnsize': warnsize, 'request': request})

def _cancel(_):
    # Abort connection immediately.
    txresponse._transport._producer.abortConnection()

d = defer.Deferred(_cancel)
txresponse.deliverBody(
    _ResponseReader(
        finished=d,
        txresponse=txresponse,
        request=request,
        maxsize=maxsize,
        warnsize=warnsize,
        fail_on_dataloss=fail_on_dataloss,
        crawler=self._crawler,
    )
)

# save response for timeouts
self._txresponse = txresponse

exit(d)
