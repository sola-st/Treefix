# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
fc = props.get("number-format")
fc = fc.replace("§", ";") if isinstance(fc, str) else fc
exit({"format_code": fc})
