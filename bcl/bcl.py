#!/usr/bin/env python3

from sys import stdin,stdout,stderr

buf = ''
tmptitle = 'THETITLESHOULDGOHERE'
linecount = 0

mainoptions = {}
suboptions = {}

def SetStyle():
    pass

def Setup():
    global buf
    buf += f"<!DOCTYPE html>\n<html>\n\t<title>{tmptitle}</title>\n\n\t<meta charset=\"UTF-8\">\n\n"
    buf += f"\t<head>\n\t\t<h1>{tmptitle}</h1>\n\t</head>\n\n"
    SetStyle()
    buf += "\t<body>\n"

def Finish():
    global buf
    buf += "\t</body>\n</html>"

def GetNextLine():
    global linecount
    line = stdin.readline()
    linecount += 1
    return line

def CheckSyntax(line):
    linearr = line.split(' ',1)

    command = linearr[0]
    if command not in mainoptions:
        stderr.write(f'Unexpected command at line {linecount}:\n{line}\n')
        exit(1)

    if command[0] in ['}']:
        stderr.write(f'Bad format: Unexpected }} at line {linecount}:\n{line}\n')
        exit(2)

    if command[0] in ['{'] and len(linearr) != 1:
        stderr.write(f'Bad format: Line {linecount} begins with {{ but has trailing characters:\n{line}\n')
        exit(3)

    if command[0] in ['|', '='] and len(linearr) != 2:
        stderr.write(f'Bad format: Line {linecount} begins with {command[0]} but is not a complete line:\n{line}\n')
        exit(4)


def SetTitle(line):
    global buf
    buf = buf.replace(tmptitle,line.split(' ',1)[1])

def NewSection(line):
    pass

def SetHeadVerse(line):
    pass

def SetVerse(line):
    pass

def NewPoint(line):
    pass

def StartSeeOther(line):
    pass

def SetTranslation(line):
    pass

def StartHeadVerse(line):
    pass

def StartVerse(line):
    pass

def FullHeadVerse(line):
    pass

def FullVerse(line):
    pass

mainoptions['|T'] = SetTitle
mainoptions['|H'] = NewSection
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

        line = line.strip()

        CheckSyntax(line)

        command = line.split(' ',1)[0]
        mainoptions[command](line)

if __name__ == "__main__":
    main()
