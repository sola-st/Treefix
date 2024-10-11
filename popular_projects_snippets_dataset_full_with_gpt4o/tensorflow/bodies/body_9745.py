# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
exit(list(
    zip([feed.values, feed.indices] if feed.dense_shape is None else
        [feed.values, feed.indices, feed.dense_shape], feed_val)))
