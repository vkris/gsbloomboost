""" S3 utilities """
import os
from config import BloomConfig

def s3_put(file_name):
    confs = BloomConfig().read_config_data()
    home_dir = confs['s3_home_dir']
    os.system('s3cmd put s3://'+home_dir+file_name)


s3_put('asdf')
