# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
referer = referer_str(request)

if response.status != 200:
    logger.warning(
        'File (code: %(status)s): Error downloading file from '
        '%(request)s referred in <%(referer)s>',
        {'status': response.status,
         'request': request, 'referer': referer},
        extra={'spider': info.spider}
    )
    raise FileException('download-error')

if not response.body:
    logger.warning(
        'File (empty-content): Empty file from %(request)s referred '
        'in <%(referer)s>: no-content',
        {'request': request, 'referer': referer},
        extra={'spider': info.spider}
    )
    raise FileException('empty-content')

status = 'cached' if 'cached' in response.flags else 'downloaded'
logger.debug(
    'File (%(status)s): Downloaded file from %(request)s referred in '
    '<%(referer)s>',
    {'status': status, 'request': request, 'referer': referer},
    extra={'spider': info.spider}
)
self.inc_stats(info.spider, status)

try:
    path = self.file_path(request, response=response, info=info, item=item)
    checksum = self.file_downloaded(response, request, info, item=item)
except FileException as exc:
    logger.warning(
        'File (error): Error processing file from %(request)s '
        'referred in <%(referer)s>: %(errormsg)s',
        {'request': request, 'referer': referer, 'errormsg': str(exc)},
        extra={'spider': info.spider}, exc_info=True
    )
    raise
except Exception as exc:
    logger.error(
        'File (unknown-error): Error processing file from %(request)s '
        'referred in <%(referer)s>',
        {'request': request, 'referer': referer},
        exc_info=True, extra={'spider': info.spider}
    )
    raise FileException(str(exc))

exit({'url': request.url, 'path': path, 'checksum': checksum, 'status': status})
