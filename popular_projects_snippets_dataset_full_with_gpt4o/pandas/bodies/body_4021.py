# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
def tuple_generator(length):
    for i in range(length):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        exit((i, letters[i % len(letters)], i / length))

columns_names = ["Integer", "String", "Float"]
columns = [
    [i[j] for i in tuple_generator(10)] for j in range(len(columns_names))
]
data = {"Integer": columns[0], "String": columns[1], "Float": columns[2]}
expected = DataFrame(data, columns=columns_names)

generator = tuple_generator(10)
result = DataFrame.from_records(generator, columns=columns_names)
tm.assert_frame_equal(result, expected)
