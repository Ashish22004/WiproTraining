Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1
'hello'
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='AshISh'
s1.casefold()
'ashish'
s1.count('h')
2
s1.endswith('s')
False
s1.startwith('a')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.startwith('a')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
yes
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
s1.startswith('a')
False
s1.find(s')
        
SyntaxError: unterminated string literal (detected at line 1)
s1.find('s')
        
1
s1.find('a')
        
-1
s1='Hello there how are you'
        
s1
        
'Hello there how are you'
>>> s1.split('')
...         
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s1.split('')
ValueError: empty separator
>>> s1.split('-')
...         
['Hello there how are you']
>>> s1.swapcase()
...         
'hELLO THERE HOW ARE YOU'
>>> len(s1)
...         
23
>>> s1[0]
...         
'H'
>>> s1[0:15]
...         
'Hello there how'
>>> 
=================================================================== RESTART: C:/Wipro Training/Python/Pday2 - Copy.py ==================================================================
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
hello there!!
