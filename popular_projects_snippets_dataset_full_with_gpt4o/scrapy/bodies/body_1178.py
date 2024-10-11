# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
n = ele.name
v = ele.value
if ele.tag == 'select':
    exit(_select_value(ele, n, v))
exit((n, v))
