# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Validate `enqueue_datas_list`."""

def _check_agreement(data, name, feature, enqueue_data):
    """Helper function to check device agreement."""
    if (data is not None and
        data.device != enqueue_data.embedding_indices.device):
        raise ValueError('Device of {0} does not agree with that of'
                         'embedding_indices for feature {1}.'.format(
                             name, feature))

feature_set = set(self._feature_to_config_dict.keys())
contiguous_device = None
for i, enqueue_datas in enumerate(enqueue_datas_list):
    used_feature_set = set(enqueue_datas.keys())

    # Check features are valid.
    missing_feature_set = feature_set - used_feature_set
    if missing_feature_set:
        raise ValueError('`enqueue_datas_list[{}]` misses a feature that is '
                         'in `feature_to_config_dict`: {}.'.format(
                             i, missing_feature_set))

    extra_feature_set = used_feature_set - feature_set
    if extra_feature_set:
        raise ValueError('`enqueue_datas_list[{}]` has a feature that is not '
                         'in `feature_to_config_dict`: {}.'.format(
                             i, extra_feature_set))

    device = None
    device_feature = None
    for feature, enqueue_data in enqueue_datas.items():
        combiner = self._table_to_config_dict[
            self._feature_to_config_dict[feature].table_id].combiner

        if isinstance(enqueue_data, EnqueueData):
            if enqueue_data.sample_indices is None and combiner:
                logging.warn(
                    'No sample indices set for features %f table %f but '
                    'combiner is set to %s.', feature,
                    self._feature_to_config_dict[feature].table_id, combiner)
            _check_agreement(enqueue_data.sample_indices, 'sample_indices',
                             feature, enqueue_data)
            _check_agreement(enqueue_data.aggregation_weights,
                             'aggregation_weights', feature, enqueue_data)

        elif isinstance(enqueue_data, RaggedEnqueueData):
            if enqueue_data.row_splits is None and combiner:
                logging.warn(
                    'No row splits set for features %f table %f but '
                    'combiner is set to %s.', feature,
                    self._feature_to_config_dict[feature].table_id, combiner)
            _check_agreement(enqueue_data.row_splits, 'row_splits', feature,
                             enqueue_data)
            _check_agreement(enqueue_data.aggregation_weights,
                             'aggregation_weights', feature, enqueue_data)
        else:
            raise ValueError(
                '`enqueue_datas_list[{}]` has a feature that is not mapped to '
                '`EnqueueData` or `RaggedEnqueueData`. `feature`: {}'.format(
                    i, feature))
        # Check all features are on the same device.
        if device is None:
            device = enqueue_data.embedding_indices.device
            device_feature = feature
        else:
            if device != enqueue_data.embedding_indices.device:
                raise ValueError('Devices are different between features in '
                                 '`enqueue_datas_list[{}]`; '
                                 'devices: {}, {}; features: {}, {}.'.format(
                                     i, device,
                                     enqueue_data.embedding_indices.device, feature,
                                     device_feature))

    if i % self._num_cores_per_host:
        if device != contiguous_device:
            raise ValueError('We expect the `enqueue_datas` which are on the '
                             'same host to be contiguous in '
                             '`enqueue_datas_list`, '
                             '`enqueue_datas_list[{}]` is on device {}, '
                             'but is expected to be on device {}.'.format(
                                 i, device, contiguous_device))
    else:
        contiguous_device = device
