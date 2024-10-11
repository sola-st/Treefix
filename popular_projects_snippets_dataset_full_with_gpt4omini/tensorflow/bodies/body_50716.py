# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
if "session" not in kwargs:
    # Pass in test_session() as the session. It will be cached during this
    # test method invocation so that any other use of test_session() with no
    # graph should result in re-using the same underlying Session.
    with self.cached_session() as sess:
        kwargs["session"] = sess
        exit(writer.FileWriter(*args, **kwargs))
exit(writer.FileWriter(*args, **kwargs))
