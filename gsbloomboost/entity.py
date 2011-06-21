#import gsbloomboost 
from config import BloomConfig
from bloom import Bloom
import elementtree.ElementTree as ETree
#import gsbloomboost.config.BloomConfig
#import gsbloomboost.bloom.Bloom

class Entity:
    """
    A class to manipulate the charlotte's 400 list.
    """


    # An inverted index for searching entities.
    entities_file = None
    sources_file = None
    default = None
    lookup = {}
    bucket_list = []  # This should ideally be a set
    bucket_lookup = {}

    def __init__(self,entities_file, sources_file):
        """ 
        Generate an inverted index here.
        Should ideally use two files, the xml file containing negative Ids
        and the charlott's list
        The resultant hash if of hte form -id->[list of elements]
        """
        self.entities_file = entities_file
        self.sources_file  = sources_file
#        self.default = default
        self.create_inverted_index()
        self.create_bucket_lookup()
        print self.lookup

        
    def create_inverted_index(self):
        """
        Create an inverted index based on the file
        """
        # Code for entities file is obsolete
        """
        for line in file(self.entities_file):
            if line.startswith('#'): continue
            entities = line.strip().split(',')
            self.bucket_list.append(entities[0])
            for entity in entities[1:]: # First element is the bucket name
                # entity points to a bloom filter object.
                self.lookup[entity.strip()] = entities[0]
        """
        # Code using the xml fiel
        tree = ETree.ElementTree(file=self.sources_file)
        # Get all source elements
        sources = tree.findall('source')
        # Parse sources.
        idd = ""
        for elements in sources:
            for element in elements:
                if ( element.tag == 'title' ):
                    idd = element.text
                    ## Append the titles to a list - These are the bucket names.
                    self.bucket_list.append(idd)
                elif ( element.tag == 'tags'):
                    tags = element.findall('tag')
                    for tag in tags:
                        text = self.beautify(tag.text)
                        self.lookup[text] = idd

    def beautify(self, text):
        return text.strip('"""')


    def create_bucket_lookup(self):
        """
        Mapping between entity and blooom fileter object
        """
        for element in self.bucket_list:
            element = '_'.join(element.split())
            self.bucket_lookup[element] = Bloom("../input/filters/"+element+".bloom")

    def get_elements(self):
        """
        Get the list of elements for a particular id
        """
        pass

    def get_bucket_name(self, entity):
        """
        Returns the bucket name given an entity; If not available returns default bucket name
        """
        try:
            return lookup[entity]
        except KeyError: 
            return default
    
    def add_to_filter(self, element, user_name):
        try:
            entity = self.lookup[element]
            bf = self.bucket_lookup[entity]
            bf.add_elements(user_name)
            print "Adding to filter"
        except KeyError:
            print "Not adding to filter :  No Match"
            pass

    def save_all(self):
        for bf in self.bucket_lookup.itervalues():
            bf.close()


if __name__ == "__main__":

    conf = BloomConfig().read_config_data()
    entities_file = conf['entities_file']
    sources_file = conf['sources_file']
    default = conf['default_entity']
    
    e = Entity(entities_file, sources_file)
    e.add_to_filter("#HappinessTruck","vivek")
    e.add_to_filter("Porsche","jdev")
    e.add_to_filter("Porsche","surya")
    e.add_to_filter("Honda","surya")
    e.add_to_filter("coca-la","surya")


    e.save_all()


