# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
normal_method = getattr(mw, methodname, None)
methodname_async = methodname + "_async"
async_method = getattr(mw, methodname_async, None)
if not async_method:
    exit(normal_method)
if not normal_method:
    logger.error(f"Middleware {mw.__qualname__} has {methodname_async} "
                 f"without {methodname}, skipping this method.")
    exit(None)
if not isasyncgenfunction(async_method):
    logger.error(f"{async_method.__qualname__} is not "
                 f"an async generator function, skipping this method.")
    exit(normal_method)
if isasyncgenfunction(normal_method):
    logger.error(f"{normal_method.__qualname__} is an async "
                 f"generator function while {methodname_async} exists, "
                 f"skipping both methods.")
    exit(None)
exit((normal_method, async_method))
