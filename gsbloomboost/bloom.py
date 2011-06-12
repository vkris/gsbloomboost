# Class to deal with bloom filter.
import pybloomfilter

class Bloom:
    file_name = ""
    def create_bloom(self, file_name):
        """ If global file exists create a new file using the template 
            else download from s3 and create a new file using the template.
            Set the class variale to this file name
        """
        pass
    def add_element(self):
        """ Add an element to this file name
        """
        pass
    def save_bloom(self):
        """ Save the bloom file
        """
        pass
    def merge(self, merge_file_name, new_file_name):
        """ Basically a union of two bloom filters.
        """
        pass


if __name__ == '__main__':
    pass
