# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
if self._finished.called:
    exit()

if reason.check(ResponseDone):
    self._finish_response()
    exit()

if reason.check(PotentialDataLoss):
    self._finish_response(flags=["partial"])
    exit()

if reason.check(ResponseFailed) and any(r.check(_DataLoss) for r in reason.value.reasons):
    if not self._fail_on_dataloss:
        self._finish_response(flags=["dataloss"])
        exit()

    if not self._fail_on_dataloss_warned:
        logger.warning("Got data loss in %s. If you want to process broken "
                       "responses set the setting DOWNLOAD_FAIL_ON_DATALOSS = False"
                       " -- This message won't be shown in further requests",
                       self._txresponse.request.absoluteURI.decode())
        self._fail_on_dataloss_warned = True

self._finished.errback(reason)
