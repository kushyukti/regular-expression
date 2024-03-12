import re as regex

text_to_search = '''abcdefghijklmnopqrstiuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr.Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr . T 

'''
sentence = 'Start a sentence and then bring it to an end'

print ('1.',r'\tab')

pattern = regex.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
matches1 = pattern.findall(text_to_search)

# for match in matches:
#   print('2.',match)

# for match in matches1:
#   print('3.',match)


# pattern2 = regex.compile(r'.')
# matches2 = pattern2.finditer(text_to_search)

# for match in matches2:
#   print('3.',match)


pattern3 = regex.compile(r'\d\d\d')
pattern4 = regex.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches3 = pattern3.finditer(text_to_search)
matches4 = pattern4.finditer(text_to_search)

for match in matches3:
  print('4.',match)

for match in matches4:
  print('5.',match)


# for 