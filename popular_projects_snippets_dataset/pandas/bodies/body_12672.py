# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
string_input = "A string \\ / \b \f \n \r \t </script> &"
not_html_encoded = '"A string \\\\ \\/ \\b \\f \\n \\r \\t <\\/script> &"'
html_encoded = (
    '"A string \\\\ \\/ \\b \\f \\n \\r \\t \\u003c\\/script\\u003e \\u0026"'
)

def helper(expected_output, **encode_kwargs):
    output = ujson.encode(
        string_input, ensure_ascii=ensure_ascii, **encode_kwargs
    )

    assert output == expected_output
    assert string_input == json.loads(output)
    assert string_input == ujson.decode(output)

# Default behavior assumes encode_html_chars=False.
helper(not_html_encoded)

# Make sure explicit encode_html_chars=False works.
helper(not_html_encoded, encode_html_chars=False)

# Make sure explicit encode_html_chars=True does the encoding.
helper(html_encoded, encode_html_chars=True)
