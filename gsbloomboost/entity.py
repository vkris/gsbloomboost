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
    bucket_list = []

    def __init__(self):
        """ 
        Generate an inverted index here.
        Should ideally use two files, the xml file containing negative Ids
        and the charlott's list
        The resultant hash if of hte form -id->[list of elements]
        """
        self.create_inverted_index()

        
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
                self.lookup[entity] = Bloom("/tmp/"+entities[0]+".bloom")

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


if __name__ == "__main__":
    Entity()

