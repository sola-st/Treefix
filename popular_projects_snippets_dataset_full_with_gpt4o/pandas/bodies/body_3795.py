# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
exit(DataFrame(
    {
        "a": ["a", "b", "c", "d", "e"],
        "c": ["meow", "bark", "um... weasel noise?", "nay", "chirp"],
    },
    index=range(5),
).set_index("a"))
