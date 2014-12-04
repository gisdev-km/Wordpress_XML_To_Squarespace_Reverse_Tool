''' 
    Wordpress to Squarespace XML Reversal Tool
    
    Author:  Kyle Morgan (@gisdev_km)
    Date:    12/4/2014

    Requirements: Python

    Purpose: Squarespace imports blog posts from Wordpress XML format in the order as 
             listed in the file.  This quick script reverses the order listed for
             chronological display when importing into Squarespace.

'''


import os

file = r"<path to file>.xml"

def main():
    
    xmlData = open(file).readlines()

    items = {}

    print 'Opening output file'
    target = os.path.join(os.path.dirname(file),"{0}_fixed.xml".format(os.path.basename(file)[:-4]))

    print 'Processing XML file'
    f = open(target, 'w')
    f.writelines(xmlData[0:42])
    
    startLine = -999
    endLine = -999
    
    for x, data in enumerate(xmlData):
        line = data.strip()
        if line.startswith("<item>"):
            startLine = x
        
        if line.startswith("</item>"):
            endLine = x
            
        if startLine > 0 and endLine > 0:
            key = len(items)
            items[key+1] = xmlData[startLine:endLine+1]
            startLine, endLine = -999, -999

    print 'Writing to file'
    for key in reversed(sorted(items)):
        f.writelines(items[key])        

    print 'Closing file'
    f.writelines(xmlData[-2:])
    f.close()

if __name__ == "__main__":
    main()