import yaml
import re


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def parse_yaml_file():
    travis_file_raw = open('./.travis.yml').read()
    travis_file_parsed = yaml.safe_load(travis_file_raw)
    # jobs_raw = travis_file_parsed['env']['jobs']
    # jobs = []
    # for job in jobs_raw:
    #     jobs.append(to_camel_case(job[14:-5].lower()))
    # print jobs
    scripts_raw = travis_file_parsed['script']
    # m = re.search('--(.+?)--', scripts_raw)
    pattern = re.compile(r'--(.+?)--')
    # matches = pattern.finditer(scripts_raw)

    # for match in matches:
    #     print(match.group())
    raw_suites = []
    for script in scripts_raw:
        matches = pattern.finditer(script)
        for match in matches:
            raw_suites.append(match.group()[9:-4])
        # print script

    for item in raw_suites:
        print item


if __name__ == "__main__":
    parse_yaml_file()
