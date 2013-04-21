import os
import sys

# 솔루션을 빌드하는데 사용되는 옵션들 저장

isStatic = False

qtFrameworkOpts = {}

qtFrameworkOpts[ 'qtVersion' ] = '5.0.1'
qtFrameworkOpts[ 'qtFileExtension' ] = 'zip'
qtFrameworkOpts[ 'qtFrameworkFilenamePattern' ] = 'qt-everywhere-opensource-src-%(qtVersion)s'
qtFrameworkOpts[ 'qtFrameworkFileName' ] = qtFrameworkOpts[ 'qtFrameworkFilenamePattern' ] % qtFrameworkOpts
qtFrameworkOpts[ 'qtFrameworkURLPattern' ] = 'http://download.qt-project.org/official_releases/qt/5.0/%(qtVersion)s/single/%(qtFrameworkFileName)s.%(qtFileExtension)s'
qtFrameworkOpts[ 'qtFrameworkURL' ] = qtFrameworkOpts[ 'qtFrameworkURLPattern' ] % qtFrameworkOpts

qtFrameworkOpts

buildOpts = {}

scriptFolder = 'scripts'
archiveFolder = 'archives'
workFolder = 'work'
