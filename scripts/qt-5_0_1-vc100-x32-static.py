
import util
import os
import buildOptions
import zipfile
import subprocess

# 필요한 패키지 목록
requirePackages = [ 'sqlite' ]
requirePatches = [ 'qmake.conf.no.pdb.make.patch' ]

buildOptions.qtFrameworkOpts[ 'qtFrameworkURL' ] = buildOptions.qtFrameworkOpts[ 'qtFrameworkURLPattern' ] % buildOptions.qtFrameworkOpts

fileName = buildOptions.qtFrameworkOpts[ 'qtFrameworkFileName' ]

def prepare():
    pass

def src_download():
    fileURL = buildOptions.qtFrameworkOpts[ 'qtFrameworkURL' ]
    print( 'Qt Framework downloading...' )

    if( util.downloadFileFromWeb( fileURL, os.path.join( os.curdir, buildOptions.archiveFolder ) ) == True ):
        print( 'Qt Framework download completed.' )
        subprocess.call( 
                        [ 'touch.exe', 
                         os.path.join( os.path.abspath( os.path.join( os.curdir, buildOptions.archiveFolder ) ), fileName ) 
                         ] )
    else:
        print( 'Qt Framework download failed.' )

def src_unpack():
    frameworkFolder = os.path.abspath( os.path.join( os.curdir, buildOptions.workFolder ) )
    if( os.path.exists( frameworkFolder ) == False ):
        os.mkdir( frameworkFolder )

    frameworkFilePath = os.path.abspath( os.path.join( os.path.join( os.curdir, buildOptions.archiveFolder ), buildOptions.qtFrameworkOpts[ 'qtFrameworkFileName' ] ) ) + '.' + buildOptions.qtFrameworkOpts[ 'qtFileExtension' ]
    print( frameworkFilePath  )

    print( 'Qt Framework Zip File Openning...' )
    z = zipfile.ZipFile( frameworkFilePath, 'r' )
    print( 'Qt Framework Zip File Opened.' )

    print( 'Qt Framework extracting...' )
    z.extractall( frameworkFolder )
    print( 'Qt Framework extracted.' )
    z.close()

    subprocess.call( 
                    [ 'touch.exe', 
                     os.path.join( os.path.abspath( os.path.join( os.curdir, buildOptions.workFolder ) ), fileName + '.unpacked' )
                     ] )
    pass

def src_packages():
    for packageItem in requirePackages:
        pass
    
    pass

def src_patch():
    oldCurrDir = os.path.abspath( os.curdir )
    
    os.chdir( os.path.join( os.path.join( os.curdir, buildOptions.workFolder ) ), fileName ) 
    
    for patchItem in requirePatches:
        print( patchItem )
        pass
    
    os.chdir( oldCurrDir )
    pass

