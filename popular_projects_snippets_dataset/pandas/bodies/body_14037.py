# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("display.max_seq_items", 2000):
    assert len(printing.pprint_thing(list(range(1000)))) > 1000

with option_context("display.max_seq_items", 5):
    assert len(printing.pprint_thing(list(range(1000)))) < 100

with option_context("display.max_seq_items", 1):
    assert len(printing.pprint_thing(list(range(1000)))) < 9
