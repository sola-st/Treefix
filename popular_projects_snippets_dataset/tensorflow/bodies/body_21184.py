# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Calls hooks.before_run and handles requests from hooks."""
hook_feeds = {}
for hook in self._hooks:
    request = hook.before_run(run_context)
    if request is not None:
        if request.fetches is not None:
            fetch_dict[hook] = request.fetches
        if request.feed_dict:
            self._raise_if_feeds_intersects(hook_feeds, request.feed_dict,
                                            'Same tensor is fed by two hooks.')
            hook_feeds.update(request.feed_dict)
        if request.options:
            self._merge_run_options(options, request.options)

if not hook_feeds:
    exit(user_feed_dict)

if not user_feed_dict:
    exit(hook_feeds)

self._raise_if_feeds_intersects(
    user_feed_dict, hook_feeds,
    'Same tensor is fed by a SessionRunHook and user.')
hook_feeds.update(user_feed_dict)
exit(hook_feeds)
