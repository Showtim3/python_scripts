import os


def check_http_present(file_path):
    test_file = open(file_path).read()
    if test_file.find('$http.') != -1 or test_file.find('HttpClient') != -1:
        return True


def get_all_services():
    path = os.path.abspath('/Users/apple/codebase/opensource/oppia/core/templates/dev/head/')
    print path

    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            http = check_http_present(os.path.join(root, name))
            if http:
                print(os.path.join(root, name))
                print name
        # for name in dirs:
        #     print '--------------------------------------------'
        #     print name
        #     print '--------------------------------------------'


if __name__ == "__main__":
    get_all_services()
    # path ='/Users/apple/codebase/opensource/oppia/core/templates/dev/head/services/stateful/focus-manager.service.ts'
    # check_http_present(path)