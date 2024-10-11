# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
if not extra_feed_dict:
    exit(new_feeds)
r = {}
r.update(extra_feed_dict)
r.update(new_feeds)
exit(r)
