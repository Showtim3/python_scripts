import re
import json

sentence = 'Start a sentence and bring it to an end'

dataFile = open("test/config/protractor.conf.js")
protractContent = dataFile.read()

helperRegex = 'suites = {([^}]+)}'
pattern = re.compile(r'suites = {([^}]+)}')
matches = pattern.finditer(protractContent)

for match in matches:
    # print(match.group())
    suite = match.group()
    # print(json.loads(match.group()))

print(suite)
# print((match.start(), match.end()), match.group(), match.end())