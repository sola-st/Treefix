# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
"""Check partitions of a parquet file are as expected.

    Parameters
    ----------
    path: str
        Path of the dataset.
    expected: iterable of str
        Expected partition names.
    """
if pa_version_under6p0:
    import pyarrow.parquet as pq

    dataset = pq.ParquetDataset(path, validate_schema=False)
    assert len(dataset.partitions.partition_names) == len(expected)
    assert dataset.partitions.partition_names == set(expected)
else:
    import pyarrow.dataset as ds

    dataset = ds.dataset(path, partitioning="hive")
    assert dataset.partitioning.schema.names == expected
