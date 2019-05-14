#!/usr/bin/env python3

from sys import stdin,stdout,stderr

buf = ''
tmptitle = 'THETITLESHOULDGOHERE'
linecount = 0

mainoptions = {}
suboptions = {}

def Setup():
    global buf
    buf += f"<!DOCTYPE html>\n<html>\n\t<title>{tmptitle}</title>\n\n\t<meta charset=\"UTF-8\">\n\n"
    buf += f"\t<head>\n\t\t<h1>{tmptitle}</h1>\n\t</head>\n\n"
    # put in style tags here
    buf += "\t<body>\n"

def Finish():
    global buf
    buf += "\t</body>\n</html>"

def GetNextLine():
    global linecount
    line = stdin.readline()
    linecount += 1
    return line

def SetTitle(title):
    global buf
    buf = buf.replace(tmptitle,title)

def SetHeadVerse():
    pass

def SetVerse():
    pass

def NewPoint():
    pass

def StartSeeOther():
    pass

def SetTranslation():
    pass

def StartHeadVerse():
    pass

def StartVerse():
    pass

def FullHeadVerse():
    pass

def FullVerse():
    pass

mainoptions['|T'] = SetTitle
mainoptions['|V'] = SetHeadVerse
mainoptions['|v'] = SetVerse
mainoptions['|p'] = NewPoint
mainoptions['{c'] = StartSeeOther

suboptions['|t'] = SetTranslation
suboptions['{V'] = StartHeadVerse
suboptions['{v'] = StartVerse
suboptions['=V'] = FullHeadVerse
suboptions['=v'] = FullVerse



def main():
    global mainoptions
    global buf

    Setup()

    while True:
        line = GetNextLine()

        if not line:
            Finish()
            print(buf)
            break

        if ' ' not in line:
            stderr.write(f'Bad format at line {linecount}:\n{line}')
            exit(1)

        command,realline = line.strip().split(' ',1)
        if command not in mainoptions:
            stderr.write(f'Unexpected command at line {linecount}:\n{line}')
            exit(2)

        mainoptions[command](realline)

if __name__ == "__main__":
    main()
