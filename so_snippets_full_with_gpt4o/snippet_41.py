# Extracted from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
}

print 'Master is currently {RED}red{END}!'.format(**formatters)
print 'Help make master {GREEN}green{END} again!'.format(**formatters)

