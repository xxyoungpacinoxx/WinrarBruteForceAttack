from subprocess import check_output
import itertools
import config
import string
from datetime import datetime

# this is Password Found Flag
password_found = False

# Error Characters "&\'(),-.:;<=>?[\\]^`{|}~
password_list = string.ascii_letters + string.digits + r'!@#$%+/_*'


# range(Minimum Digit, Maximum Digit)
# Example --> Minimum Digit (2 --> a,b,c,...,*) | Maximum Digit (5 --> aaaaa,...,*_/+%)
start_time = datetime.now()
for item in range(1, 17):
    generator = itertools.product(password_list, repeat=item)

    for password in generator:
        try:
            # check Password File by check_output
            check_output(fr'"{config.UNRAR_FILE_ADRESS}" x test.rar -p' + ''.join(password), shell=True)
            print(f"password find! --> {''.join(password)}")
            password_found = True
            break
        except:
            print(f" --> {''.join(password)}")
            continue
    if password_found is True:
        break

end_time = datetime.now()

duration = end_time - start_time
print(f'duration: {duration}')
