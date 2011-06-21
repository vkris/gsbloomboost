from ConfigParser import SafeConfigParser
import logging
import logging.handlers


class BloomConfig:
    """ A class to parse the configuration file """
    config = {}
    def __init__(self, config_file='../input/config.txt'):
        config = SafeConfigParser()
        config.read(config_file)

        self.config['aws_key']    = config.get('S3','aws-key')
        self.config['aws_secret'] = config.get('S3','aws-secret')
        self.config['s3_home_dir'] = config.get('S3','s3-home-dir')

        self.config['global_file_name'] = config.get('Bloom','global-file-name')
        self.config['local_file_name']  = config.get('Bloom','local-file-name')
        self.config['local_dir']  = config.get('Bloom','local-dir')
        self.config['template_file_name']  = config.get('Bloom','template-file-name')
        self.config['local_filter_dir']  = config.get('Bloom','local-filter-dir')

        self.config['entities_file']  = config.get('Entity','entities-file')
        self.config['default_entity']  = config.get('Entity','default-entity')

        self.config['sources_file'] = config.get('Sources','sources-file')

    @classmethod
    def read_config_data(self):
        """ method to read the configuration data"""
        return self.config



if __name__ == '__main__':
    bc = BloomConfig('../input/config.txt')
    print bc.read_config_data()
