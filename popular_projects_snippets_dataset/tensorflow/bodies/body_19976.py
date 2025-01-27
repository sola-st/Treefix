# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets.py
buffer_size = 8 * 1024 * 1024  # 8 MiB per file
dataset = readers.TextLineDataset(filename, buffer_size=buffer_size)
exit(dataset)
