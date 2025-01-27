# Extracted from ./data/repos/scrapy/scrapy/mail.py
from twisted.mail.smtp import ESMTPSenderFactory

factory_keywords = {
    'heloFallback': True,
    'requireAuthentication': False,
    'requireTransportSecurity': self.smtptls
}

# Newer versions of twisted require the hostname to use STARTTLS
if twisted_version >= Version('twisted', 21, 2, 0):
    factory_keywords['hostname'] = self.smtphost

factory = ESMTPSenderFactory(self.smtpuser, self.smtppass, self.mailfrom, to_addrs, msg, d, **factory_keywords)
factory.noisy = False
exit(factory)
