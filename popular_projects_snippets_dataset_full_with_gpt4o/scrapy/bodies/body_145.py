# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
if isinstance(result, Failure):
    # minimize cached information for failure
    result.cleanFailure()
    result.frames = []
    result.stack = None

    # This code fixes a memory leak by avoiding to keep references to
    # the Request and Response objects on the Media Pipeline cache.
    #
    # What happens when the media_downloaded callback raises an
    # exception, for example a FileException('download-error') when
    # the Response status code is not 200 OK, is that the original
    # StopIteration exception (which in turn contains the failed
    # Response and by extension, the original Request) gets encapsulated
    # within the FileException context.
    #
    # Originally, Scrapy was using twisted.internet.defer.returnValue
    # inside functions decorated with twisted.internet.defer.inlineCallbacks,
    # encapsulating the returned Response in a _DefGen_Return exception
    # instead of a StopIteration.
    #
    # To avoid keeping references to the Response and therefore Request
    # objects on the Media Pipeline cache, we should wipe the context of
    # the encapsulated exception when it is a StopIteration instance
    #
    # This problem does not occur in Python 2.7 since we don't have
    # Exception Chaining (https://www.python.org/dev/peps/pep-3134/).
    context = getattr(result.value, '__context__', None)
    if isinstance(context, StopIteration):
        setattr(result.value, '__context__', None)

info.downloading.remove(fp)
info.downloaded[fp] = result  # cache result
for wad in info.waiting.pop(fp):
    defer_result(result).chainDeferred(wad)
