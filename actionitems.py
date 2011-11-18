__author__ = 'adewinter'

import sys

def printUsage():
    msg = '''
    Action Items:
    Takes in a Ryan Format txt file. Spits out Actionable Items and Items marked for follow up query.
    Usage:
    ./actionitems.py [notesfilename]
     '''
    print msg
    
def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print 'No filename specified!'
        printUsage()
        sys.exit(1)
    filename = argv[1]
    
    file = open(filename)

    actionItems = []
    queryItems = []

    for line in file:
        if line.find('A:') != -1:
            actionItems.append(line)

        if line.find('Q:') != -1:
            queryItems.append(line)

    print 'Found %s Action Items:' % len(actionItems)
    for item in actionItems:
        print '\t %s' % item.strip()

    print '========================'

    print 'Found %s Query Items:' % len(queryItems)
    for item in queryItems:
        print '\t %s' % item.strip()
    


if __name__ == "__main__":
    main()