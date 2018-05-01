from ar import parseArchiveFile

def testValidSignature():
    parseArchiveFile('test.a')

def testInvalidSignature():
    parseArchiveFile('README.md')

testValidSignature()
testInvalidSignature()
