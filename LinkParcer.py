import getopt, re, sys
from BeautifulSoup import BeautifulSoup

def parse(html):
    digest = html[html.find("<br>"):]
    digest = digest[4:]
    html = BeautifulSoup(html)
    title = html.a.string
    link = html.a.href
    pr_info = title[title.find("(")+1:title.find(")")]
    dt = ['','','']
    dt = pr_info.split(", ")        # authors, date, place
    title =  title[0:title.find("(")]
    inner = BeautifulSoup(digest)
    pattern =r'<(a|/a).*?>'    
    for a in inner.findAll('a', href=True):
        lnk = "[" + a.string + "==" + a['href'] + "]"
        print lnk.encode('utf-8')
        print str(a)
        digest = re.sub(pattern, "*", digest)
        digest = digest.replace("*"+str(a.string)+"*", lnk.encode('utf-8'))

    # for el in BeautifulSoup(digest).a:
    #     print el.href
    print 
    print "\"Title\": \"" + title + "\","
    print "\"Link\": \"" + html.a['href'] + "\","
    print "\"InfoID\": \"article\","
    print "\"InfoDate\": \"" + dt[1] + "\","
    print "\"InfoAuthors\": \"" + dt[0] + "\","
    print "\"InfoID\": \"\","
    print "\"InfoPlace\": \"" + dt[2] + "\","
    print "\"Digest\": \"" + digest + "\""

def main(argv):
    try:
        opts, arg = getopt.getopt(argv, "t:", ["txt="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        arg.rstrip("\n\r")
        if opt in ("-t", "--txt"):
            parse(arg)
        else:
            print "no HTML input"

if __name__ == '__main__':
    main(sys.argv[1:])
