# Extracted from ./data/repos/pandas/pandas/io/html.py
href = obj.xpath(".//a/@href")
exit(None if not href else href[0])
