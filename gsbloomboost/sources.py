from config import BloomConfig
import elementtree.ElementTree as ETree
import os

class Sources:
    """
    You may need to install ElementTree library.  Download source and run `python setup.py install`
    A class to sync charlotte's list and sources.xml file .
    """

    id1 = 0
    root = None

    def __init__(self, csv_file, xml_file):        
        self.csv_file = csv_file
        self.xml_file = xml_file
        pass

    def generate(self):
        # Get the entities from the csv file
        elements = [ line.split(',')[0] for line in file(self.csv_file) if not line.startswith('#') ] 
        self.generate_xml(elements)
        self.save()
        pass

    def generate_xml(self, elements):
        self.root     = ETree.Element('sources')
        self.root.attrib = { 'xmlns:xsi' : 'http://www.w3.org/2001/XMLSchema-instance' } 
#        ETree.register_namespace('xsi','http://www.w3.org/2001/XMLSchema-instance')
        for element in elements:
            self.add_node(element)

    def add_node(self,element):
        source   = ETree.SubElement(self.root, "source")
        iid      = ETree.SubElement(source,"id")
        self.id1 = self.id1 - 1
        iid.text = str(self.id1)

        status         = ETree.SubElement(source,"status")
        status.text    = "active"

        title          = ETree.SubElement(source,"title")
        title.text     = element

        internal_name  = ETree.SubElement(source,"internal_name")
        internal_name.text = "twitter_users_category"

    def save(self):
        tree = ETree.ElementTree(self.root)
        tree.write('../input/temp_sources.xml','utf-8',xml_declaration=True)
        # Tidy look for xxml
        os.system('bash ../scripts/tidy_xml.sh ../input/temp_sources.xml ' + self.xml_file )

    def validate(self):
        ## Reports if xml file and csv file are in sync
        csv_elements =  [ line.split(',')[0] for line in file(self.csv_file) if not line.startswith('#') ]
        xml_elements = self.parse_elements()
        # Returns if both the lists are same. 
        return set(csv_elements) == set(xml_elements) 


    def parse_elements(self):
        tree = ETree.ElementTree(file=xml_file)
        nodes = tree.findall('source/title')
        elements = [ element.text for element in nodes ] 
        return elements

    def update(self):
        pass


if __name__ == '__main__':

    conf = BloomConfig().read_config_data()
    csv_file = conf['entities_file']
    xml_file = conf['sources_file']

    s = Sources(csv_file, xml_file)
    #s.generate()
    print s.validate()
