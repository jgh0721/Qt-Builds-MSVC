'''
Created on 2013. 4. 14.

@author: DevTester
'''
import util
import os
import buildOptions

sqliteVersion = '3071602'
sqliteURL = 'http://www.sqlite.org/2013/sqlite-amalgamation-%s.zip' % sqliteVersion

def prepare():
    pass

def src_download():
    util.downloadFileFromWeb( sqliteURL, os.path.join( os.path.curdir, buildOptions.archiveFolder ) )
    pass

def src_unpack():
    
    pass

def src_patch():
    pass
 