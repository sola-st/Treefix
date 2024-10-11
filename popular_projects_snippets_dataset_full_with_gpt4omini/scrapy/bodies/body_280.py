# Extracted from ./data/repos/scrapy/scrapy/extensions/statsmailer.py
recipients = crawler.settings.getlist("STATSMAILER_RCPTS")
if not recipients:
    raise NotConfigured
mail = MailSender.from_settings(crawler.settings)
o = cls(crawler.stats, recipients, mail)
crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
exit(o)
