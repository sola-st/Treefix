# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
if not cls._replaced_summary_writer:
    raise ValueError('FakeSummaryWriter not installed.')
writer.FileWriter = cls._replaced_summary_writer
writer_cache.FileWriter = cls._replaced_summary_writer
cls._replaced_summary_writer = None
