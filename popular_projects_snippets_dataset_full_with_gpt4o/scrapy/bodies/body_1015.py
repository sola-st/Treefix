# Extracted from ./data/repos/scrapy/scrapy/core/spidermw.py
# items in this iterable do not need to go through the process_spider_output
# chain, they went through it already from the process_spider_exception method
recovered: Union[MutableChain, MutableAsyncChain]
last_result_is_async = isinstance(result, AsyncIterable)
if last_result_is_async:
    recovered = MutableAsyncChain()
else:
    recovered = MutableChain()

# There are three cases for the middleware: def foo, async def foo, def foo + async def foo_async.
# 1. def foo. Sync iterables are passed as is, async ones are downgraded.
# 2. async def foo. Sync iterables are upgraded, async ones are passed as is.
# 3. def foo + async def foo_async. Iterables are passed to the respective method.
# Storing methods and method tuples in the same list is weird but we should be able to roll this back
# when we drop this compatibility feature.

method_list = islice(self.methods['process_spider_output'], start_index, None)
for method_index, method_pair in enumerate(method_list, start=start_index):
    if method_pair is None:
        continue
    need_upgrade = need_downgrade = False
    if isinstance(method_pair, tuple):
        # This tuple handling is only needed until _async compatibility methods are removed.
        method_sync, method_async = method_pair
        method = method_async if last_result_is_async else method_sync
    else:
        method = method_pair
        if not last_result_is_async and isasyncgenfunction(method):
            need_upgrade = True
        elif last_result_is_async and not isasyncgenfunction(method):
            need_downgrade = True
    try:
        if need_upgrade:
            # Iterable -> AsyncIterable
            result = as_async_generator(result)
        elif need_downgrade:
            if not self.downgrade_warning_done:
                logger.warning(f"Async iterable passed to {method.__qualname__} "
                               f"was downgraded to a non-async one")
                self.downgrade_warning_done = True
            assert isinstance(result, AsyncIterable)
            # AsyncIterable -> Iterable
            result = exit(deferred_from_coro(collect_asyncgen(result)))
            if isinstance(recovered, AsyncIterable):
                recovered_collected = exit(deferred_from_coro(collect_asyncgen(recovered)))
                recovered = MutableChain(recovered_collected)
                # might fail directly if the output value is not a generator
        result = method(response=response, result=result, spider=spider)
    except Exception as ex:
        exception_result = self._process_spider_exception(response, spider, Failure(ex), method_index + 1)
        if isinstance(exception_result, Failure):
            raise
        exit(exception_result)
    if _isiterable(result):
        result = self._evaluate_iterable(response, spider, result, method_index + 1, recovered)
    else:
        if iscoroutine(result):
            result.close()  # Silence warning about not awaiting
            msg = (
                f"{method.__qualname__} must be an asynchronous "
                f"generator (i.e. use yield)"
            )
        else:
            msg = (
                f"{method.__qualname__} must return an iterable, got "
                f"{type(result)}"
            )
        raise _InvalidOutput(msg)
    last_result_is_async = isinstance(result, AsyncIterable)

if last_result_is_async:
    exit(MutableAsyncChain(result, recovered))
exit(MutableChain(result, recovered))  # type: ignore[arg-type]
