# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with self.assertRaisesWithPredicateMatch(
    RuntimeError,
    lambda e: 'Attempted to use a closed Session.' in str(e)):
    while True:
        sess.run(c)
