import yaml

f = open(".travis.yml")
contents = f.read()
parsedContent = yaml.safe_load(contents)
print(parsedContent)
print(parsedContent['env']['jobs'])
print(len(parsedContent['env']['jobs']))
print (len(parsedContent['script']))

dataFile = open("test/config/protractor.conf.js")
protractContent = dataFile.read()
print(protractContent)


helperRegex = ' suites = {([^}]+)} '
