import re
import json
# classroom page is missing from both
sentence = 'Start a sentence and bring it to an end'

dataFile = open("test/config/protractor.conf.js")
protractContent = dataFile.read()

suitesRegex = 'suites = {([^}]+)}'
commentsRegex = '(//.*)'

pattern = re.compile(r'suites = {([^}]+)}')
matches = pattern.finditer(protractContent)

for match in matches:
    # print(match.group())
    suite = match.group()
    # print(json.loads(match.group()))

# print(suite)

pattern2 = re.compile(r'(//.*)')
matches2 = pattern2.finditer(suite)
rawObj = re.sub(pattern2, '', suite)
# print rawObj

finalObj = rawObj[10:-1]
# print finalObj
print finalObj.count(':')

# print(finalObj.split(':'))
words = finalObj.strip().split('\n')
keys = []
i = 0
a = ['.js', '[', ']']
while i < len(words):
    # print(i, words[i])
    keyRaw = words[i].strip().split(':')[0]
    if not any(x in keyRaw for x in a) and len(keyRaw) != 0:
        keys.append(keyRaw)
    i += 1
# print words

i = 0
while i < len(keys):
    print i, keys[i]
    i += 1
# for word in finalObj.split(':'):
#     print word
# pattern = re.compile(r'(?<=\\w)(.*?)(?=:)')
# matches3 = pattern.finditer(finalObj)
#
# for match in matches3:
#     print match.group()

# dict(s.split(':', 1) for s in finalObj.split())

# print finalObj
# print(json.loads(finalObj))
# print json.loads(json.dumps(rawObj))
# print((match.start(), match.end()), match.group(), match.end())