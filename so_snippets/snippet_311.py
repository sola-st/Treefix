# Extracted from https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
import re
s = "string. With. Punctuation?" # Sample string 
out = re.sub(ur'[^\w\d\s]+', '', s)

