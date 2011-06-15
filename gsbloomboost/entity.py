from config import BloomConfig
from bloom import Bloom

class Entity:
    """
    A class to manipulate the charlotte's 400 list.
    """
    conf = BloomConfig().read_config_data()
    entities_file = conf['entities_file']
    default = conf['default_entity']

    # An inverted index for searching entities.
    lookup = {}
    bucket_list = []  # This should ideally be a set
    bucket_lookup = {}

    def __init__(self):
        """ 
        Generate an inverted index here.
        Should ideally use two files, the xml file containing negative Ids
        and the charlott's list
        The resultant hash if of hte form -id->[list of elements]
        """
        self.create_inverted_index()
        self.create_bucket_lookup()
        print self.lookup

        
    def create_inverted_index(self):
        """
        Create an inverted index based on the file
        """
        for line in file(self.entities_file):
            if line.startswith('#'): continue
            entities = line.strip().split(',')
            self.bucket_list.append(entities[0])
            for entity in entities[1:]: # First element is the bucket name
                # entity points to a bloom filter object.
                self.lookup[entity.strip()] = entities[0]

    def create_bucket_lookup(self):
        """
        Mapping between entity and blooom fileter object
        """
        for element in self.bucket_list:
            self.bucket_lookup[element] = Bloom("/tmp/"+element+".bloom")

    def get_elements(self):
        """
        Get the list of elements for a particular id
        """

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
    e = Entity()
    e.add_to_filter("Porsche","sdfs")
    e.add_to_filter("Porsche","jdev")
    e.add_to_filter("Porsche","surya")
    e.add_to_filter("Honda","surya")
    e.add_to_filter("coca-la","surya")


    e.save_all()


