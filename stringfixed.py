import time

def strcat(string):
    newstr = ''
    for char in string:
        newstr += string
    return newstr

def listcat(string):
    return ''.join([char for char in string])

def test(fn, times, *args):
    start = time.time()
    for x in xrange(times):
        fn(*args)
    return time.time() - start

def testall():
    strings = ['a', 'long', 'longer', 'a bit longer', 
               '''adjkrsn widn fskejwoskemwkoskdfisdfasdfjiz  oijewf sdkjjka dsf sdk siasjk dfwijs''',
               '''this is a really long string that's so long
               it had to be triple quoted  and contains lots of
               superflous characters for kicks and gigles
               @!#(*_#)(*$(*!#@&)(*E\xc4\x32\xff\x92\x23\xDF\xDFk^%#$!)%#^(*#''',
              '''I needed another long string but this one won't have any new lines or crazy characters in it, I'm just going to type normal characters that I would usually write blah blah blah blah this is some more text hey cool what's crazy is that it looks that the str += is really close to the O(n^2) worst case performance, but it looks more like the other method increases in a perhaps linear scale? I don't know but I think this is enough text I hope.''']

    print 'Testing fixed join'
    for string in strings:
        print "String of len:", len(string), "took:", test(listcat, 1000000, string), "seconds"
    print 'Testing + concat'
    for string in strings:
        print "String of len:", len(string), "took:", test(strcat, 1000000, string), "seconds"
    print 'Testing Complete'
testall()
