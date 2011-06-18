#from gsbloomboost import util 
from gsbloomboost.entity import Entity
from gsbloomboost.config import BloomConfig
from gsbloomboost.bloom import Bloom
import os

from nose import with_setup

def setup():
    conf = BloomConfig().read_config_data()
    entities_file = conf['entities_file']
    sources_file = conf['sources_file']
    default = conf['default_entity']
    
    e = Entity(entities_file, sources_file)
    e.add_to_filter("Porsche","sdfs")
    e.add_to_filter("Porsche","jdev")
    e.add_to_filter("Porsche","surya")
    e.add_to_filter("Honda","surya")
    e.add_to_filter("coca-la","surya")
    #os.system('touch /tmp/jumbli.txt')

def teardown():
    pass
    #os.system('rm /tmp/jumbli.txt')

def test_main():
    bf = Bloom('../input/filters/Cars.bloom')
#    bf2 = Bloom('../input/Phone.bloom')

    result =  [ bf.has_element("sdfs") and bf.has_element('jdev') and
                bf.has_element('surya') ]
    print result 
    assert result 

