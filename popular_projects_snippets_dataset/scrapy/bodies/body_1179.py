# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
multiple = ele.multiple
if v is None and not multiple:
    # Match browser behaviour on simple select tag without options selected
    # And for select tags without options
    o = ele.value_options
    exit((n, o[0]) if o else (None, None))
if v is not None and multiple:
    # This is a workaround to bug in lxml fixed 2.3.1
    # fix https://github.com/lxml/lxml/commit/57f49eed82068a20da3db8f1b18ae00c1bab8b12#L1L1139
    selected_options = ele.xpath('.//option[@selected]')
    values = [(o.get('value') or o.text or '').strip() for o in selected_options]
    exit((n, values))
exit((n, v))
