""" S3 utilities """
import os
from config import BloomConfig

class S3Util:
    conf = BloomConfig().read_config_data()
    home_dir = conf['s3_home_dir']
    local_dir = conf['local_dir']

    @classmethod
    def s3_put(self,file_name):
        #os.system('s3cmd put s3://'+home_dir+file_name)
        print 's3cmd put s3://'+self.home_dir+file_name
    
    @classmethod
    def s3_get(self,file_name):
        print 's3cmd get s3://'+self.home_dir+' '+self.local_dir+file_name
        pass

if __name__ == '__main__':
    S3Util.s3_put('asdf')
    S3Util.s3_get('asdf')

