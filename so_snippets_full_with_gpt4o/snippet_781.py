# Extracted from https://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules
from json import JSONDecoder
jd = JSONDecoder()
jd.decode("""{ "a":"b" }""")
{u'a': u'b'}

from simplejson import JSONDecoder
jd = JSONDecoder()
jd.decode("""{ "a":"b" }""")
{'a': 'b'}

from simplejson import JSONDecoder
jd = JSONDecoder()
jd.decode(unicode("""{ "a":"b" }""", "utf-8"))
{u'a': u'b'}

jd.decode(unicode("""{ "a": "ξηθννββωφρες" }"""))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xce in position 8: ordinal not in range(128)

