from config import BloomConfig
import elementtree.ElementTree as ETree
import os, sys

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
        self.preprocess_windows_file()
        # rstrip to remove trailing commas.
        elements = [ line.strip().rstrip(',').split(',')[0] for line in file(self.csv_file) if not line.startswith('#') ] 
        tags = [ line.strip().rstrip(',').split(',')[1:] for line in file(self.csv_file) if not line.startswith('#') ]
        self.generate_xml(elements,tags)
        self.save()

    def preprocess_windows_file(self):
        # Remove the ctrl M character 
        os.system('tr "\015" "\n" <' + self.csv_file + ' > ../input/tmp_csv.csv')
        os.system('mv ../input/tmp_csv.csv ' + csv_file)


    def generate_xml(self, elements,tags):
        self.root     = ETree.Element('sources')
        self.root.attrib = { 'xmlns:xsi' : 'http://www.w3.org/2001/XMLSchema-instance' } 
#        ETree.register_namespace('xsi','http://www.w3.org/2001/XMLSchema-instance')
        for element,tagz in zip(elements,tags):
            self.add_node(element,tagz)

    def add_node(self,element,tags):
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

        tags_xml = ETree.SubElement(source, "tags")
        for tag in tags:
            tag_xml = ETree.SubElement(tags_xml, "tag")
            tag_xml.text = tag

    def save(self):
        tree = ETree.ElementTree(self.root)
        tree.write('../input/temp_sources.xml','utf-8',xml_declaration=True)
        # Tidy look for xxml
        os.system('bash ../scripts/tidy_xml.sh ../input/temp_sources.xml ' + self.xml_file )

    def validate(self):
        ## Reports if xml file and csv file are in sync
        csv_elements, xml_elements = self.get_csv_elements(), self.get_xml_elements("title")
        # Returns if both the lists are same. 
        return set(csv_elements) == set(xml_elements) 

    def get_csv_elements(self):
        elements =  [ line.split(',')[0] for line in file(self.csv_file) if not line.startswith('#') ]
        return elements

    def get_xml_elements(self, tag_name):        
        tree = ETree.ElementTree(file=self.xml_file)
        nodes = tree.findall('source/' + tag_name)
        elements = [ element.text for element in nodes ] 
        return elements

    def update(self):
        if ( not self.validate()):
           csv_elements, xml_elements = self.get_csv_elements(), self.get_xml_elements("title")
           diff = set(csv_elements) - set(xml_elements)
           xml_ids_str = self.get_xml_elements("id")        
           # Convert string to integer
           xml_ids = [ int(idx) for idx in xml_ids_str ]  
           
           # min because we are dealing with negative integers.
           self.id1 = min(xml_ids)   

           self.root = ETree.ElementTree(file=self.xml_file).getroot()
           for element in diff:
               tags = [ line.strip().split(',')[1:] for line in file(self.csv_file) if not line.startswith('#') and line.startswith(element) ]
               self.add_node(element,tags[0])

           self.save()
            


if __name__ == '__main__':

    conf = BloomConfig().read_config_data()
    csv_file = conf['entities_file']
    xml_file = conf['sources_file']

    s = Sources(csv_file, xml_file)
    s.generate()
    #print s.validate()
    #s.update()
    #print s.validate()
