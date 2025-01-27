# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
wrapped = SqlDatasetV2(driver_name, data_source_name, query, output_types)
super(SqlDatasetV1, self).__init__(wrapped)
