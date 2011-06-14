# Class to deal with bloom filter.
import pybloomfilter
import util
from config import BloomConfig

class Bloom:
    file_name = ""
    bloom_filter = None
    conf = BloomConfig().read_config_data()
    template_file = conf['template_file_name']
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.create_bloom()

    def create_bloom(self):
        """ If global file exists create a new file using the template 
            else download from s3 and create a new file using the template.
            Set the class variale to this file name
        """
        # Check if the template exists
        if (util.if_file_exists(self.template_file)):
            # Open the existing file
            bf = pybloomfilter.BloomFilter.open(self.template_file)
            # Create a copy of this template..
            bf.copy_template(self.file_name)
            self.bloom_filter = bf
        else:
            # Create a new bloom filter file and save its as template
            bf = pybloomfilter.BloomFilter(100000, 0.1, self.template_file)
            # Copy the template to a new file
            self.bloom_filter = bf.copy_template(self.file_name)
            
    def add_elements(self,elements):
        """ Add element(s) to this file name
        """
        if (isinstance(elements,basestring)):
            ## Just a single string
            self.bloom_filter.add(elements)
            return
        for element in elements:
            self.bloom_filter.add(element)
    
    def has_element(self, element):
        # To check if an element is available in the filter..
        return element in self.bloom_filter

    def save_bloom(self):
        """ Save the bloom file
        """
        pass
    def merge(self, merge_filter):
        """ Basically a union of two bloom filters.
        """
        self.bloom_filter.union(merge_filter.get_bloom_instance())
        pass

    def get_bloom_instance(self):
        """
        Returns the bloom filter instance for merging
        """
        return self.bloom_filter

# Testing code. 
if __name__ == '__main__':
    bf = Bloom("/tmp/test11.bloom")
    bf.add_elements(['apple','orange'])
    print bf.has_element('apple')
    print bf.has_element('teste1')

    bf2 = Bloom("/tmp/test21.bloom")
    bf2.add_elements(['teste1'])
    bf.merge(bf2)
    print bf.has_element('teste1')


