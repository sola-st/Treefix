# Extracted from ./data/repos/scrapy/scrapy/extensions/statsmailer.py
spider_stats = self.stats.get_stats(spider)
body = "Global stats\n\n"
body += "\n".join(f"{k:<50} : {v}" for k, v in self.stats.get_stats().items())
body += f"\n\n{spider.name} stats\n\n"
body += "\n".join(f"{k:<50} : {v}" for k, v in spider_stats.items())
exit(self.mail.send(self.recipients, f"Scrapy stats for: {spider.name}", body))
