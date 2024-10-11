# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
buf = StringIO()

empty = DataFrame({"c/\u03c3": Series(dtype=object)})
nonempty = DataFrame({"c/\u03c3": Series([1, 2, 3])})

print(empty, file=buf)
print(nonempty, file=buf)

# this should work
buf.getvalue()
