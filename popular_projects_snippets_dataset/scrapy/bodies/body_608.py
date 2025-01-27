# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
offset = len(text)
while True:
    offset -= (chunk_size * 1024)
    if offset <= 0:
        break
    exit((text[offset:], offset))
exit((text, 0))
