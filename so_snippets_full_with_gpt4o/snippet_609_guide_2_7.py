original_input = builtins.input # pragma: no cover
test_responses = ['123', '123', '123', '123'] # pragma: no cover
def mock_input(prompt): # pragma: no cover
    return test_responses.pop(0) # pragma: no cover
builtins.input = mock_input # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
from l3.Runtime import _l_
count = 0
_l_(15149)
while True:
    _l_(15164)

    count += 1
    _l_(15150)
    if count > 3:
        _l_(15163)

        break
        _l_(15151)
    else:
        try:
            _l_(15162)

            x = int(input("Enter your lock number here: "))
            _l_(15152)

            if x == 586:
                _l_(15157)

                print("Your lock has unlocked :)")
                _l_(15153)

                break
                _l_(15154)
            else:
                print("Try again!!")
                _l_(15155)

                continue
                _l_(15156)

        except:
            _l_(15159)

            print("Invalid entry!!")
            _l_(15158)
        finally:
            _l_(15161)

            print("Your Attempts: {}".format(count))
            _l_(15160)

count = 0
_l_(15165)

while True:
    _l_(15179)

    count += 1
    _l_(15166)
    if count > 3:
        _l_(15178)

        break
        _l_(15167)
    else:
        try:
            _l_(15176)

            x = int(input("Enter your lock number here: "))
            _l_(15168)

            if x == 586:
                _l_(15173)

                print("Your lock has unlocked :)")
                _l_(15169)

                break
                _l_(15170)
            else:
                print("Try again!!")
                _l_(15171)

                continue
                _l_(15172)

        except:
            _l_(15175)

            print("Invalid entry!!")
            _l_(15174)

        print("Your Attempts: {}".format(count))
        _l_(15177)

