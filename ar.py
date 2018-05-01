AR_SIGNATURE = '!<arch>'
AR_SIGNATURE_LENGTH = len(AR_SIGNATURE)

def hasValidSignature(content):
    return content[:AR_SIGNATURE_LENGTH] == AR_SIGNATURE

def parseArchiveFile(fileName):
    fd = open(fileName)
    content = fd.read()

    if not hasValidSignature(content):
        print('ar signature ' + AR_SIGNATURE + ' not found while parsing ' + fileName)
