# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
super(DistributedTableTest, cls).tearDownClass()
cls.cluster.stop()
