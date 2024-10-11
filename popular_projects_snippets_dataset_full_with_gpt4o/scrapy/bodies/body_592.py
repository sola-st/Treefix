# Extracted from ./data/repos/scrapy/scrapy/utils/signal.py
"""Like pydispatcher.robust.sendRobust but it also logs errors and returns
    Failures instead of exceptions.
    """
dont_log = named.pop('dont_log', ())
dont_log = tuple(dont_log) if isinstance(dont_log, collections.abc.Sequence) else (dont_log,)
dont_log += (StopDownload, )
spider = named.get('spider', None)
responses = []
for receiver in liveReceivers(getAllReceivers(sender, signal)):
    try:
        response = robustApply(receiver, signal=signal, sender=sender, *arguments, **named)
        if isinstance(response, Deferred):
            logger.error("Cannot return deferreds from signal handler: %(receiver)s",
                         {'receiver': receiver}, extra={'spider': spider})
    except dont_log:
        result = Failure()
    except Exception:
        result = Failure()
        logger.error("Error caught on signal handler: %(receiver)s",
                     {'receiver': receiver},
                     exc_info=True, extra={'spider': spider})
    else:
        result = response
    responses.append((receiver, result))
exit(responses)
