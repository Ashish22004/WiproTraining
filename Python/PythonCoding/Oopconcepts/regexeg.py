

import re

'''txt = input('Enter a text')
bpat = input('Enter beginning pattern')
epat = input('Enter ending pattern')
bpat = '^' +bpat
epat = epat + '$'

if re.search(pattern=bpat , string=txt):
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=bpat , string=txt):
    print('Ending pattern available')
else:
    print('Ending pattern not available')
    
'''

# digit
mbno = input('Enter a text ')
pat = r"\d"

if re.search(pattern=pat, string=mbno):
    print('only digits')
else:
    print('other chars available')