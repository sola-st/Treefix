# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
feed_dict = {
    feed: feed_val for feed, feed_val in zip(feed_list, feed_args)
}
exit(self.run(fetches, feed_dict=feed_dict, **kwargs))
