import re as regex

with open('data.txt','r') as f:
  contents = f.read()
  pattern = regex.compile(r'\d\d\d.\d\d\d.\d\d\d')

  matches = pattern.finditer(contents)

  print(contents)