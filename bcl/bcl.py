#!/usr/bin/env python3

from sys import stdin,stdout,stderr

buf = ''
tmptitle = 'THETITLESHOULDGOHERE'

mainoptions = {}
# mainoptions['|T'] =
# mainoptions['|V'] =
# mainoptions['|v'] =
# mainoptions['|p'] =
# mainoptions['{c'] =
#
# suboptions = {}
# suboptions['|t'] =
# suboptions['{V'] =
# suboptions['{v'] =

def Setup():
    global buf
    buf += "<!DOCTYPE html>\n<html>\n\t<title>" + tmptitle + "</title>\n\n\t<meta charset=\"UTF-8\">\n\n"
    # put in style tags here
    buf += "\t<body>\n"

def Finish():
    global buf
    buf += "\t</body>\n</html>"



def main():
    Setup()

    while True:
        line = stdin.readline()

        if not line:
            Finish()
            print(buf)
            break

        command,line = line.strip().split(' ',1)
        # if command[0] not in ['|', '{', '=']:



if __name__ == "__main__":
    main()
