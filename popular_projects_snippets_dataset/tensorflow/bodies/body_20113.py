# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Create mapping from table to a list of its features."""
table_to_features_dict_tmp = {}
for feature, feature_config in feature_to_config_dict.items():
    if feature_config.table_id in table_to_features_dict_tmp:
        table_to_features_dict_tmp[feature_config.table_id].append(feature)
    else:
        table_to_features_dict_tmp[feature_config.table_id] = [feature]

table_to_features_dict = collections.OrderedDict()
for table in sorted(table_to_features_dict_tmp):
    table_to_features_dict[table] = sorted(table_to_features_dict_tmp[table])
exit(table_to_features_dict)
