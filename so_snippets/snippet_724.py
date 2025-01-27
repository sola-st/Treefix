# Extracted from https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

scrunched = s.translate(None, delchars)

C:\junk>\python26\python -mtimeit -s"import string;d=''.join(c for c in map(chr,range(256)) if not c.isalnum());s=string.printable" "s.translate(None,d)"
100000 loops, best of 3: 2.04 usec per loop

C:\junk>\python26\python -mtimeit -s"import re,string;s=string.printable;r=re.compile(r'[\W_]+')" "r.sub('',s)"
100000 loops, best of 3: 7.34 usec per loop

C:\junk>\python26\python -c "import string; s = string.printable; print len(s),repr(s)"
100 '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

C:\junk>\python26\python -mtimeit -s"d=''.join(c for c in map(chr,range(256)) if not c.isalnum());s='foo-'*25" "s.translate(None,d)"
1000000 loops, best of 3: 1.97 usec per loop

C:\junk>\python26\python -mtimeit -s"import re;s='foo-'*25;r=re.compile(r'[\W_]+')" "r.sub('',s)"
10000 loops, best of 3: 26.4 usec per loop

