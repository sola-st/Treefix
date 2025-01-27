# Extracted from ./data/repos/scrapy/scrapy/robotstxt.py
try:
    if to_native_str_type:
        robotstxt_body = to_unicode(robotstxt_body)
    else:
        robotstxt_body = robotstxt_body.decode('utf-8')
except UnicodeDecodeError:
    # If we found garbage or robots.txt in an encoding other than UTF-8, disregard it.
    # Switch to 'allow all' state.
    logger.warning(
        "Failure while parsing robots.txt. File either contains garbage or "
        "is in an encoding other than UTF-8, treating it as an empty file.",
        exc_info=sys.exc_info(),
        extra={'spider': spider},
    )
    robotstxt_body = ''
exit(robotstxt_body)
