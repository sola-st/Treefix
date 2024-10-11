# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
c = Categorical(["aaaaa", "bb", "cccc"] * 20)
expected = """\
['aaaaa', 'bb', 'cccc', 'aaaaa', 'bb', ..., 'bb', 'cccc', 'aaaaa', 'bb', 'cccc']
Length: 60
Categories (3, object): ['aaaaa', 'bb', 'cccc']"""

assert repr(c) == expected

c = Categorical(["ああああ", "いいいいい", "ううううううう"] * 20)
expected = """\
['ああああ', 'いいいいい', 'ううううううう', 'ああああ', 'いいいいい', ..., 'いいいいい', 'ううううううう', 'ああああ', 'いいいいい', 'ううううううう']
Length: 60
Categories (3, object): ['ああああ', 'いいいいい', 'ううううううう']"""  # noqa:E501

assert repr(c) == expected

# unicode option should not affect to Categorical, as it doesn't care
# the repr width
with option_context("display.unicode.east_asian_width", True):

    c = Categorical(["ああああ", "いいいいい", "ううううううう"] * 20)
    expected = """['ああああ', 'いいいいい', 'ううううううう', 'ああああ', 'いいいいい', ..., 'いいいいい', 'ううううううう', 'ああああ', 'いいいいい', 'ううううううう']
Length: 60
Categories (3, object): ['ああああ', 'いいいいい', 'ううううううう']"""  # noqa:E501

    assert repr(c) == expected
