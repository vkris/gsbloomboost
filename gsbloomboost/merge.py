
import os,sys
from bloom import Bloom

def get_files(folder):
    walk = os.walk(folder)
    info = walk.next()
    dirs = info[0]
    subdirs = info[1]
    files = info[2]
    files = [ dirs+"/"+file for file in files ]

    return files


def call_main(lists_folder, bloom_folder):
    list_files  = get_files(lists_folder)
    #bloom_files = get_files(bloom_folder)

    for filee in list_files:
        # Create a new bloom filter file if it does not exist..
        #Get abc in /Users/xya/asdf/abc.2bloom
        file_name = filee.rsplit('/',1)[1].split('.')[0]
        bf = Bloom(bloom_folder+"/"+file_name+".bloom")
        # Get the list of elements from the file. 
        list_of_authors = [ element.strip() for element in file(filee) ]
        print list_of_authors
        # Now start adding elements
        bf.add_elements(list_of_authors)



if __name__ == "__main__":
    if ( len(sys.argv) != 3 ):
        print "Usage python merge.py input_lists_folder bloom_filters_folder"
        sys.exit(0)
    # Before this make sure you ahve the files from s3 downloaded.......
    call_main(sys.argv[1], sys.argv[2])
