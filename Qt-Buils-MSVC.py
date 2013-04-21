# -*- coding: utf-8 -*-

__author__ = 'Jung'

import os
import sys
import argparse
import buildOptions
import subprocess

# 본 빌드 스크립트는 GitHub 의 Qt-Builds 스크립트를 참조로 하여 제작되었습니다. 

# 스크립트의 tools 폴더를 환경변수 PATH 에 등록하여 손쉽게 실행이 가능하도록 함 
os.environ[ 'PATH' ] = os.path.abspath( os.path.join( os.curdir, buildOptions.scriptFolder ) ) + ';' + os.environ[ 'PATH' ]

# 폴더 존재확인 및 생성
if( os.path.exists( os.path.join( os.path.abspath(os.curdir), buildOptions.archiveFolder ) ) == False ):
    os.mkdir( os.path.join( os.path.abspath(os.curdir), buildOptions.archiveFolder ) )
if( os.path.exists( os.path.join( os.path.abspath(os.curdir), buildOptions.workFolder ) ) == False ):
    os.mkdir( os.path.join( os.path.abspath(os.curdir), buildOptions.workFolder ) )

# 모듈 검색 경로 추가    
sys.path.append( os.path.join( os.path.abspath( os.curdir ), buildOptions.scriptFolder ) )

scriptPattern = {}
scriptPattern['qt'] = 'qt-%(qtversion)s-%(compiler)s-%(platform)s-%(static)s'

argParser = argparse.ArgumentParser( description='Qt Solution Build Script Usage, Ver. 0.1' )

argParser.add_argument( '-compiler', action='store', default='vc100', choices=( 'vc90', 'vc100', 'vc110xp' ), help='Type of MSVC' )
argParser.add_argument( '-platform', action='store', default='x32', choices=( 'x32', 'x64' ), help='Type of Build Platform' )
argParser.add_argument( '-static', action='store_true', default=True, help='Whether static build Qt Frameworks' )
argParser.add_argument( '-qtversion', action='store', default='5.0.1', choices=( '5.0.0', '5.0.1' ), help='Qt Framework Version to build' )

args = argParser.parse_args()

if( len(sys.argv) <= 1 ):
    argParser.print_help()

buildOptions.qtFrameworkOpts[ 'qtVersion' ] = args.qtversion
buildOptions.qtFrameworkOpts[ 'qtFrameworkFileName' ] = buildOptions.qtFrameworkOpts[ 'qtFrameworkFilenamePattern' ] % buildOptions.qtFrameworkOpts

buildOptions.buildOpts = { 'qtversion' : args.qtversion, 'compiler' : args.compiler, 'platform' : args.platform, 
               'static' : 'static' if args.static == True else 'non-static' }

"""
    빌드하려는 파이썬 스크립트 이름을 생성하여 해당 모듈을 import 한다. 
"""
pythonSolutionName = scriptPattern['qt'] % buildOptions.buildOpts
pythonSolutionName = pythonSolutionName.replace( '.', '_' )
print( '파이썬 빌드 파일 : ' + pythonSolutionName )

moduleSolution = __import__( pythonSolutionName )

moduleSolution.src_download()
moduleSolution.src_unpack()
moduleSolution.src_patch()

"""
dirScriptFolder = os.path.join( os.curdir, buildOptions.scriptFolder )
lstFiles = os.listdir( dirScriptFolder  )
for item in lstFiles:
    next = os.path.join( dirScriptFolder, item )
    # 바이트 코드 컴파일된 오브젝트 파일은 건너뛴다. 
    if( next.endswith( '.pyc' ) == True ):
        continue
    print( next )

    #moduleName = os.path.splitext( item )[0]
    #module = __import__( moduleName )
    #module.src_download()
    #module.src_unpack()
"""

