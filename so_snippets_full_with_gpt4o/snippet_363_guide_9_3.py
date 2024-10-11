import re # pragma: no cover
import unicodedata # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
from l3.Runtime import _l_
try:
    import re
    _l_(14987)

except ImportError:
    pass
try:
    import unicodedata
    _l_(14989)

except ImportError:
    pass

def strip_accents(text):
    _l_(14998)

    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        _l_(14993)

        text = unicode(text, 'utf-8')
        _l_(14990)
    except (TypeError, NameError):
        _l_(14992)

        pass
        _l_(14991)
    text = unicodedata.normalize('NFD', text)
    _l_(14994)
    text = text.encode('ascii', 'ignore')
    _l_(14995)
    text = text.decode("utf-8")
    _l_(14996)
    aux = str(text)
    _l_(14997)
    return aux

def text_to_id(text):
    _l_(15003)

    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text.lower())
    _l_(14999)
    text = re.sub('[ ]+', '_', text)
    _l_(15000)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    _l_(15001)
    aux = text
    _l_(15002)
    return aux

text_to_id("Montréal, über, 12.89, Mère, Françoise, noël, 889")
_l_(15004)
'montreal_uber_1289_mere_francoise_noel_889'
_l_(15005)

