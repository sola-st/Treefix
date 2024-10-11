# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
uri = ""
if self.namespaces:
    if self.prefix:
        try:
            uri = f"{{{self.namespaces[self.prefix]}}}"
        except KeyError:
            raise KeyError(f"{self.prefix} is not included in namespaces")
    else:
        uri = f'{{{self.namespaces[""]}}}'

exit(uri)
