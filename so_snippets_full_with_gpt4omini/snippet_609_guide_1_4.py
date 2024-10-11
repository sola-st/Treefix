from unittest.mock import patch # pragma: no cover

input = patch('builtins.input', side_effect=['123', '456', '586']).start() # pragma: no cover
print = lambda msg: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
from l3.Runtime import _l_
count = 0
_l_(3175)
while True:
    _l_(3190)

    count += 1
    _l_(3176)
    if count > 3:
        _l_(3189)

        break
        _l_(3177)
    else:
        try:
            _l_(3188)

            x = int(input("Enter your lock number here: "))
            _l_(3178)

            if x == 586:
                _l_(3183)

                print("Your lock has unlocked :)")
                _l_(3179)

                break
                _l_(3180)
            else:
                print("Try again!!")
                _l_(3181)

                continue
                _l_(3182)

        except:
            _l_(3185)

            print("Invalid entry!!")
            _l_(3184)
        finally:
            _l_(3187)

            print("Your Attempts: {}".format(count))
            _l_(3186)

count = 0
_l_(3191)

while True:
    _l_(3205)

    count += 1
    _l_(3192)
    if count > 3:
        _l_(3204)

        break
        _l_(3193)
    else:
        try:
            _l_(3202)

            x = int(input("Enter your lock number here: "))
            _l_(3194)

            if x == 586:
                _l_(3199)

                print("Your lock has unlocked :)")
                _l_(3195)

                break
                _l_(3196)
            else:
                print("Try again!!")
                _l_(3197)

                continue
                _l_(3198)

        except:
            _l_(3201)

            print("Invalid entry!!")
            _l_(3200)

        print("Your Attempts: {}".format(count))
        _l_(3203)

