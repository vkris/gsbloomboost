import os, sys
from config import BloomConfig
from bloom import Bloom
import elementtree.ElementTree as ETree

def get_id_lookup():
    conf = BloomConfig().read_config_data()
    sources_file = conf['twitter_sources_file'] 
    # Code using the xml fiel
    tree = ETree.ElementTree(file=sources_file)
    # Get all source elements
    sources = tree.findall('source')

    lookup = {}

    for elements in sources:
        idd, title, tag = "", "", ""
        for element in elements:
            if ( element.tag == 'id' ):
                idd = element.text
            elif ( element.tag == 'title'):
                title = element.text
            elif ( element.tag == 'tags'):
                tags = element.findall('tag')
                for tag in tags:
                    tag = tag.text
        if (tag == "bloom_count"):
            lookup[title] = idd
    return lookup

def get_id(count, lookup):
    
    if (count == 0):
        return lookup['Default']

    for id_range, id in lookup.iteritems():
        if id_range in 'Default': continue
        id_start , id_end = id_range.split('-')
        if ( int(id_start) <= count <= int(id_end) ): 
            return id

    return lookup['Default']


def call_main(author_name):
    bf = Bloom()
    count = bf.search("/Users/vivekris/GS/code/gsbloomboost/input/filters/",author_name)
    lookup = get_id_lookup()

    return_id = get_id(count, lookup)
    print return_id



if __name__ == "__main__":
    if (len(sys.argv) != 2 ):
        print "Usage python find_id.py <author_name>\n Returns an Id prenset in sources.xml"
        sys.exit(0)
    call_main(sys.argv[1])
