from Frontier import Frontier
from PageRanker import PageRanker

frontier = Frontier()
pageRanker = PageRanker()

seedDocuments = [
    'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html',
    'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html',
    'http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html'
]

def printWebGraph(webGraph):
    print
    print '-*( Web Graph )*-'
    print
    for entry in sorted(webGraph.keys()):
        print entry + ' -> ' + ', '.join(webGraph[entry])


def printPageRanks(pageRanks):
    print
    print '-*( Page Ranks )*-'
    print
    print '\t\t\t\t',
    for page in sorted(pageRanks[1]):
        print '\t\t\t' + page,
    for step, pageRank in sorted(pageRanks.iteritems()):
        print
        print 'Step ' + str(step) + '\t',
        for page, rank in sorted(pageRank.iteritems()):
            print '\t\t' + '{0:.4f}'.format(rank),


webGraph = frontier.getWebGraph(seedDocuments)
pageRank = pageRanker.getPageRank(webGraph)

printWebGraph(webGraph)
printPageRanks(pageRank)

