# Start an infinite loop that receives tweet and author

# Sync with global bloom filter
import sys
from config import BloomConfig
from entity import Entity

def get_bag_of_words(tweet):
    return [word for word in tweet.strip().split()]

def main(author, tweet):
    conf = BloomConfig().read_config_data()
    entities_file = conf['entities_file']
    sources_file = conf['sources_file']
    default = conf['default_entity']
    
    e = Entity(entities_file, sources_file)
    words = get_bag_of_words(tweet)
    print words
    for word in words:
        e.add_to_filter(word, author)
#    e.add_to_filter("Porsche","sdfs")


if __name__ == "__main__":
    if (len(sys.argv) != 3 ):
        print "Usage: main.py author_name tweet"
    else:
        main(sys.argv[1], sys.argv[2])
