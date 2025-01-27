# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
super(TPUEmbeddingBaseTest, self).setUp()
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
self.feature_config = (tpu_embedding_v2_utils.FeatureConfig(
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
self.feature_watched_indices = [[0, 0], [1, 0], [1, 1], [2, 0], [2, 1],
                                [3, 0]]
self.feature_watched_values = [0, 0, 1, 0, 1, 1]
self.feature_watched_row_lengths = [1, 2, 2, 1]
# sparse tensor for favorited:
# row 0: 0, 1
# row 1: 1
# row 2: 0
# row 3: 0, 1
self.feature_favorited_indices = [[0, 0], [0, 1], [1, 0], [2, 0], [3, 0],
                                  [3, 1]]
self.feature_favorited_values = [0, 1, 1, 0, 0, 1]
self.feature_favorited_row_lengths = [2, 1, 1, 2]
# sparse tensor for friends:
# row 0: 3
# row 1: 0, 1, 2
# row 2: 3
# row 3: 0, 1, 2
self.feature_friends_indices = [[0, 0], [1, 0], [1, 1], [1, 2], [2, 0],
                                [3, 0], [3, 1], [3, 2]]
self.feature_friends_values = [3, 0, 1, 2, 3, 0, 1, 2]
self.feature_friends_row_lengths = [1, 3, 1, 3]
self.resolver = None

# Basically we are expand the dims of the old feature by 1 and repeat
# batch size times for the first dimension.
def create_hight_dimensional_indices(indices):
    indices = np.array(indices, dtype=np.int32)
    batch_size_index = np.repeat(
        np.arange(self.data_batch_size), len(indices)).reshape(-1, 1)
    repeated_indices = np.tile(indices, (self.data_batch_size, 1))
    exit(np.concatenate([batch_size_index, repeated_indices], axis=1))

# Create high dimensional features with shape(4, 4, 2)
self.feature_watched_indices_high_dimensional = create_hight_dimensional_indices(
    self.feature_watched_indices)
self.feature_watched_values_high_dimensional = self.feature_watched_values * self.data_batch_size
self.feature_watched_row_lengths_high_dimensional = self.feature_watched_row_lengths * self.data_batch_size

# Create high dimensional features with shape(4, 4, 2)
self.feature_favorited_indices_high_dimensional = create_hight_dimensional_indices(
    self.feature_favorited_indices)
self.feature_favorited_values_high_dimensional = self.feature_favorited_values * self.data_batch_size
self.feature_favorited_row_lengths_high_dimensional = self.feature_favorited_row_lengths * self.data_batch_size

# Create high dimensional features with shape(4, 4, 3)
self.feature_friends_indices_high_dimensional = create_hight_dimensional_indices(
    self.feature_friends_indices)
self.feature_friends_values_high_dimensional = self.feature_friends_values * self.data_batch_size
self.feature_friends_row_lengths_high_dimensional = self.feature_friends_row_lengths * self.data_batch_size
