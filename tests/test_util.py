from gsbloomboost import util 
import os
from nose import with_setup

def setup():
    os.system('touch /tmp/jumbli.txt')

def teardown():
    os.system('rm /tmp/jumbli.txt')

def test_util():
    # Test ifFileExists
    assert util.if_file_exists('/tmp/jumbli.txt') 

