from header import Header
from pprint import pprint

AR_SIGNATURE = '!<arch>'
AR_SIGNATURE_LENGTH = len(AR_SIGNATURE)

def hasValidSignature(content):
    return content[:AR_SIGNATURE_LENGTH] == AR_SIGNATURE

def parseArchiveFile(fileName):
    fd = open(fileName)
    content = fd.read()

    if not hasValidSignature(content):
        print('ar signature ' + AR_SIGNATURE + ' not found while parsing ' + fileName)
        return

    content = content[AR_SIGNATURE_LENGTH + 1:]

    while True:
        header, content = Header.parse_header(content)
        pprint(vars(header))

        fd_temp = open('tmp_' + header.file_identifier, 'w')
        fd_temp.write(content[:header.file_size])
        fd_temp.close()
        content = content[header.file_size:]

        if len(content) < 60:
            break;
