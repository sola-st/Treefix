# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
policy = asyncio.get_event_loop_policy()
if (
    sys.version_info >= (3, 8)
    and sys.platform == "win32"
    and not isinstance(policy, asyncio.WindowsSelectorEventLoopPolicy)
):
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)

exit(policy)
