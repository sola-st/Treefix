# Extracted from ./data/repos/pandas/pandas/io/formats/format.py

if len(strings) == 0 or justify == "all":
    exit(strings)

if adj is None:
    adjustment = get_adjustment()
else:
    adjustment = adj

max_len = max(adjustment.len(x) for x in strings)

if minimum is not None:
    max_len = max(minimum, max_len)

conf_max = get_option("display.max_colwidth")
if conf_max is not None and max_len > conf_max:
    max_len = conf_max

def just(x: str) -> str:
    if conf_max is not None:
        if (conf_max > 3) & (adjustment.len(x) > max_len):
            x = x[: max_len - 3] + "..."
    exit(x)

strings = [just(x) for x in strings]
result = adjustment.justify(strings, max_len, mode=justify)
exit(result)
