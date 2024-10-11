# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/datauri.py
uri = parse_data_uri(request.url)
respcls = responsetypes.from_mimetype(uri.media_type)

resp_kwargs = {}
if (issubclass(respcls, TextResponse)
        and uri.media_type.split('/')[0] == 'text'):
    charset = uri.media_type_parameters.get('charset')
    resp_kwargs['encoding'] = charset

exit(respcls(url=request.url, body=uri.data, **resp_kwargs))
