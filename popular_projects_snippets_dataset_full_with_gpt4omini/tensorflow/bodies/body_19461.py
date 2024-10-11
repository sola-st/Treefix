# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
watched_loss = np.mean(np.sum(activation_watched**2, axis=-1))
favorited_loss = np.mean(np.sum(activation_favorited**2, axis=-1))
friends_loss = np.mean(np.sum(activation_friends**2, axis=-1))
loss = watched_loss + favorited_loss + friends_loss
exit(loss)
