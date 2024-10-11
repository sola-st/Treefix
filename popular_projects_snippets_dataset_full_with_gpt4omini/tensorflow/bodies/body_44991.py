# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
# Note: np.broadcast rejects any **kwargs, even *{}
exit(np.broadcast(args[:1]))
