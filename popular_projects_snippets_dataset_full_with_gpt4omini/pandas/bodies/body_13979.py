# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_eng_formatting.py
formatter = fmt.EngFormatter(accuracy=3, use_eng_prefix=True)
in_out = [
    (5.55555, " 5.556"),
    (55.5555, " 55.556"),
    (555.555, " 555.555"),
    (5555.55, " 5.556k"),
    (55555.5, " 55.556k"),
    (555555, " 555.555k"),
]
self.compare_all(formatter, in_out)

formatter = fmt.EngFormatter(accuracy=1, use_eng_prefix=True)
in_out = [
    (5.55555, " 5.6"),
    (55.5555, " 55.6"),
    (555.555, " 555.6"),
    (5555.55, " 5.6k"),
    (55555.5, " 55.6k"),
    (555555, " 555.6k"),
]
self.compare_all(formatter, in_out)

formatter = fmt.EngFormatter(accuracy=0, use_eng_prefix=True)
in_out = [
    (5.55555, " 6"),
    (55.5555, " 56"),
    (555.555, " 556"),
    (5555.55, " 6k"),
    (55555.5, " 56k"),
    (555555, " 556k"),
]
self.compare_all(formatter, in_out)

formatter = fmt.EngFormatter(accuracy=3, use_eng_prefix=True)
result = formatter(0)
assert result == " 0.000"
