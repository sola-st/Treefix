# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
categorical = self.categorical

if len(categorical) == 0:
    if self.footer:
        exit(self._get_footer())
    else:
        exit("")

fmt_values = self._get_formatted_values()

fmt_values = [i.strip() for i in fmt_values]
values = ", ".join(fmt_values)
result = ["[" + values + "]"]
if self.footer:
    footer = self._get_footer()
    if footer:
        result.append(footer)

exit(str("\n".join(result)))
