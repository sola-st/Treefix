# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
data = [
    (
        "0  ",
        "                        .gitignore ",
        "     5 ",
        " \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2",
    )
]
df = DataFrame(data)

# it works!
repr(df)
