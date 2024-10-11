# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
super(TPUEmbeddingForServingTest, self).setUp()

self.embedding_values = np.array(list(range(32)), dtype=np.float64)
self.initializer = init_ops_v2.Constant(self.embedding_values)
# Embedding for video initialized to
# 0 1 2 3
# 4 5 6 7
# ...
self.table_video = tpu_embedding_v2_utils.TableConfig(
    vocabulary_size=8,
    dim=4,
    initializer=self.initializer,
    combiner='sum',
    name='video')
# Embedding for user initialized to
# 0 1
# 2 3
# 4 5
# 6 7
# ...
self.table_user = tpu_embedding_v2_utils.TableConfig(
    vocabulary_size=16,
    dim=2,
    initializer=self.initializer,
    combiner='mean',
    name='user')
self.feature_config = (
    tpu_embedding_v2_utils.FeatureConfig(
        table=self.table_video, name='watched'),
    tpu_embedding_v2_utils.FeatureConfig(
        table=self.table_video, name='favorited'),
    tpu_embedding_v2_utils.FeatureConfig(
        table=self.table_user, name='friends'))

self.batch_size = 2
self.data_batch_size = 4

# One (global) batch of inputs
# sparse tensor for watched:
# row 0: 0
# row 1: 0, 1
# row 2: 0, 1
# row 3: 1
self.feature_watched_indices = [[0, 0], [1, 0], [1, 1],
                                [2, 0], [2, 1], [3, 0]]
self.feature_watched_values = [0, 0, 1, 0, 1, 1]
self.feature_watched_row_lengths = [1, 2, 2, 1]
# sparse tensor for favorited:
# row 0: 0, 1
# row 1: 1
# row 2: 0
# row 3: 0, 1
self.feature_favorited_indices = [[0, 0], [0, 1], [1, 0],
                                  [2, 0], [3, 0], [3, 1]]
self.feature_favorited_values = [0, 1, 1, 0, 0, 1]
self.feature_favorited_row_lengths = [2, 1, 1, 2]
# sparse tensor for friends:
# row 0: 3
# row 1: 0, 1, 2
# row 2: 3
# row 3: 0, 1, 2
self.feature_friends_indices = [[0, 0], [1, 0], [1, 1], [1, 2],
                                [2, 0], [3, 0], [3, 1], [3, 2]]
self.feature_friends_values = [3, 0, 1, 2, 3, 0, 1, 2]
self.feature_friends_row_lengths = [1, 3, 1, 3]
