import xml.etree.ElementTree as ET
from sys import platform as _platform
import os
import shutil
import re

def parseXML(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    fpaths = []
    for file in root.findall('file'):
        fname = file.get('file_name')
        spath = file.get('source_path')
        dpath = file.get('destination_path')
        path = [spath, dpath, fname]
        fpaths.append(path)
    return fpaths

def osCheck():
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        return 0
    elif _platform == "win32" or _platform == "win64":
        return 1

def osPathCheck(fpaths, os):
    for path in fpaths:
        if path[0][0] == '/' and path[1][0] == '/' and os == 0:
            path.append(1)
        elif path[0][1] == ':' and path[1][1] == ':' and os == 1:
            path.append(1)
        else:
            path.append(0)
    return fpaths
        
def copyFile(fpaths, os):
    for paths in fpaths:
        if paths[3] == 1:
            if os == 0:
                src = paths[0] + r"/" + paths[2]
                dst = paths[1] + r"/" + paths[2]
                shutil.copyfile(src, dst)
                print('file' + ' ' + paths[2] + ' successfuly copied from ' + paths[0] + ' to ' + paths[1])
            elif os == 1:
                src = paths[0] + '\\' + paths[2]
                dst = paths[1] + '\\' + paths[2]
                shutil.copyfile(src, dst)
                print('file' + ' ' + paths[2] + ' successfuly copied from ' + paths[0] + ' to ' + paths[1])
            else:
                print('invalid path for file ' + paths[2])
        else:
            print('invalid path for file ' + paths[2])

if __name__ == "__main__":
    document = 'example.xml'
    fpaths = parseXML(document)
    os = osCheck()
    osPathCheck(fpaths, os)
    copyFile(fpaths, os)
    
    