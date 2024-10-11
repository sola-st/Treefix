# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.test_session() as sess:
    sess_ref = weakref.ref(sess)
    with self.cached_session(graph=None, config=None) as sess2:
        # We make sure that sess2 is sess.
        assert sess2 is sess
        # We make sure we raise an exception if we use cached_session with
        # different values.
        with self.assertRaises(ValueError):
            with self.cached_session(graph=ops.Graph()) as sess2:
                pass
        with self.assertRaises(ValueError):
            with self.cached_session(force_gpu=True) as sess2:
                pass
    # We make sure that test_session will cache the session even after the
    # with scope.
assert not sess_ref()._closed
with self.session() as unique_sess:
    unique_sess_ref = weakref.ref(unique_sess)
    with self.session() as sess2:
        assert sess2 is not unique_sess
    # We make sure the session is closed when we leave the with statement.
assert unique_sess_ref()._closed
