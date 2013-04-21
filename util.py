import urllib
import os

def downloadFileFromWeb( fileURL, localFilePath ):
    filePath = os.path.join( localFilePath, fileURL.split( '/' )[-1] )
    if( os.path.exists( filePath ) == True ):
        return True

    try:
        fp = urllib.urlopen( fileURL )

        if( fp.headers.get( "content-length" ) == None ):
            raise
        else:
            fp.close()
            urllib.urlretrieve( fileURL, filePath )
            
    except:
        return False

    return True


