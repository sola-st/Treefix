# Extracted from ./data/repos/scrapy/scrapy/mail.py
logger.info('Mail sent OK: To=%(mailto)s Cc=%(mailcc)s '
            'Subject="%(mailsubject)s" Attachs=%(mailattachs)d',
            {'mailto': to, 'mailcc': cc, 'mailsubject': subject,
             'mailattachs': nattachs})
