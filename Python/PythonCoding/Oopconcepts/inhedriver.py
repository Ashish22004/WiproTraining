from Oopconcepts.college import College

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('City: ')

project = College(ccode=cc, cname=cn, ccity=ci)

project.welcome_message()
project.display_college_details()