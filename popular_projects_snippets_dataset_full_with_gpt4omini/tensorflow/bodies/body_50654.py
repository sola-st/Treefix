# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
if cls._replaced_summary_writer:
    raise ValueError('FakeSummaryWriter already installed.')
cls._replaced_summary_writer = writer.FileWriter
writer.FileWriter = FakeSummaryWriter
writer_cache.FileWriter = FakeSummaryWriter
