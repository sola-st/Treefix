# Extracted from ./data/repos/scrapy/scrapy/mail.py
errstr = str(failure.value)
logger.error('Unable to send mail: To=%(mailto)s Cc=%(mailcc)s '
             'Subject="%(mailsubject)s" Attachs=%(mailattachs)d'
             '- %(mailerr)s',
             {'mailto': to, 'mailcc': cc, 'mailsubject': subject,
              'mailattachs': nattachs, 'mailerr': errstr})
