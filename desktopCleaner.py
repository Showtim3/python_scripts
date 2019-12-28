from os import path, listdir
import os
import shutil

FILES_TO_DELETE = [
    '.ds_store',
    '.abc',
    '.bc',
    '.idea'
]

IMAGES_EXT = [
    '.png',
    '.jpg',
    '.jpeg',
    '.gif'
]

PDF = '.pdf'

DOCUMENTS = [
    '.doc',
    '.docx',
    '.ppt',
    '.xlsx'
]

JS_TS_JSON = [
    '.js',
    '.ts',
    '.tsx',
    '.jsx',
    '.txt',
    '.json'
]

EXE_ZIP = [
    '.zip',
    '.dmg',
    '.rar'
]

TORRENTS = '.torrent'


def main():

    desktop_path = path.expanduser('~/Desktop/')
    move_to_desktop_path = path.expanduser('~/Desktop/Desktop/')
    desktop_files = listdir(desktop_path)

    if path.isdir(desktop_path + 'Desktop'):
        print 'Desktop Directory is present'
    else:
        os.mkdir(move_to_desktop_path)
        os.mkdir(move_to_desktop_path + 'images')
        os.mkdir(move_to_desktop_path + 'pdf')
        os.mkdir(move_to_desktop_path + 'documents')
        os.mkdir(move_to_desktop_path + 'js')
        os.mkdir(move_to_desktop_path + 'zip')
        os.mkdir(move_to_desktop_path + 'setup')
        os.mkdir(move_to_desktop_path + 'torrent')

    for fileName in desktop_files:
        if path.isdir(path.expanduser('~/Desktop/' + fileName)):
            continue
        if fileName.endswith(PDF):
            shutil.move(desktop_path + fileName, move_to_desktop_path + 'pdf/')
            continue
        if fileName.endswith(TORRENTS):
            shutil.move(desktop_path + fileName, move_to_desktop_path + 'torrent/')
            continue
        for deleteExt in FILES_TO_DELETE:
            if fileName.endswith(deleteExt):
                os.remove(fileName)
                print(fileName + 'deleted')
        for image in IMAGES_EXT:
            if fileName.endswith(image):
                print (desktop_path + fileName, desktop_path + 'images/')
                shutil.move(desktop_path + fileName, move_to_desktop_path + 'images/')
        for doc in DOCUMENTS:
            if fileName.endswith(doc):
                shutil.move(desktop_path + fileName, move_to_desktop_path + 'documents/')
        for jsFile in JS_TS_JSON:
            if fileName.endswith(jsFile):
                shutil.move(desktop_path + fileName, move_to_desktop_path + 'js/')
        for exe in EXE_ZIP:
            if fileName.endswith(exe):
                shutil.move(desktop_path + fileName, move_to_desktop_path + 'setup/')

        print "Cleaning Complete"


if __name__ == "__main__":
    main()
