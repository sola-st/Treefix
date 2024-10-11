# Extracted from ./data/repos/scrapy/scrapy/http/request/form.py
kwargs.setdefault('encoding', response.encoding)

if formcss is not None:
    from parsel.csstranslator import HTMLTranslator
    formxpath = HTMLTranslator().css_to_xpath(formcss)

form = _get_form(response, formname, formid, formnumber, formxpath)
formdata = _get_inputs(form, formdata, dont_click, clickdata)
url = _get_form_url(form, kwargs.pop('url', None))

method = kwargs.pop('method', form.method)
if method is not None:
    method = method.upper()
    if method not in cls.valid_form_methods:
        method = 'GET'

exit(cls(url=url, method=method, formdata=formdata, **kwargs))
