# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
"""Sets and returns the event loop with specified import path."""
policy = get_asyncio_event_loop_policy()
if event_loop_path is not None:
    event_loop_class = load_object(event_loop_path)
    event_loop = event_loop_class()
    asyncio.set_event_loop(event_loop)
else:
    try:
        with catch_warnings():
            # In Python 3.10.9, 3.11.1, 3.12 and 3.13, a DeprecationWarning
            # is emitted about the lack of a current event loop, because in
            # Python 3.14 and later `get_event_loop` will raise a
            # RuntimeError in that event. Because our code is already
            # prepared for that future behavior, we ignore the deprecation
            # warning.
            filterwarnings(
                "ignore",
                message="There is no current event loop",
                category=DeprecationWarning,
            )
            event_loop = policy.get_event_loop()
    except RuntimeError:
        # `get_event_loop` raises RuntimeError when called with no asyncio
        # event loop yet installed in the following scenarios:
        # - From a thread other than the main thread. For example, when
        #   using ``scrapy shell``.
        # - Previsibly on Python 3.14 and later.
        #   https://github.com/python/cpython/issues/100160#issuecomment-1345581902
        event_loop = policy.new_event_loop()
        asyncio.set_event_loop(event_loop)
exit(event_loop)
