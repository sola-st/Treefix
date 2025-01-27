# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
exit(pprint_thing(
    thing,
    escape_chars=("\t", "\r", "\n"),
    quote_strings=True,
    max_seq_items=max_seq_items,
))
