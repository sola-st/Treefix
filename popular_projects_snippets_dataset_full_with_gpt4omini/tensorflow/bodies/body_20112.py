# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Create a per feature list of combiners, ordered by table."""
combiners = []
for table in table_to_config_dict:
    combiner = table_to_config_dict[table].combiner or 'sum'
    combiners.extend([combiner] * len(table_to_features_dict[table]))
exit(combiners)
