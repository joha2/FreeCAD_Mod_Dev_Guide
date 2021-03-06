SourceFolder=[
("3rdParty","Third party code integration",
"""boost.CMakeLists.txt  CxImage  Pivy-0.5  zlib.CMakeLists.txt CMakeLists.txt   Pivy  salomesmesh"""),
("Base","Foundamental classes for FreeCAD",
"""import as FreeCAD in Python,  see detailed description in later section"""),
("App","nonGUI code: Document, Property and DocumentObject",
"""import as FreeCAD in Python, see detailed description in later section"""),
("Gui","Qt-based GUI code: macro-recording, Workbench",
"""import as FreeCADGui in Python, see detailed description in later section"""),
("CXX","modified PyCXX containing both python 2 and python 3"),
("Main","main() function for FreeCADCmd.exe and FreeCADGui.exe",
""""Main() of FreeCADCmd.exe (build up CAD model without GUI but python scripting) and FreeCADGui.exe (Interactive mode)"""),
("Mod","Source code for all modules with each module in one subfolder",
"""Source code of ome modules will be explained in later section"""),
("Tools","Tool to build the source code: fcbt.py",
"""fcbt can generate a basic module from _TEMPLATE_ folder, """),
("Doc","Manual and documentaton"),
("CMakeLists.txt","topmost CMake config file, kind of high level cross-platform makefile generater",
"""
Module developer needs not to care about this file, CMakeLists.txt within module will be automatically included.
"""),
("FCConfig.h","preprocessor shared by all source for portability on diff platforms"),
("fc.sh","export environment variable for CASROOT -> OpenCASCADE",
"""
Module developer needs not to care about this file
"""),
("Build","set the version of FreeCAD"),
("MacAppBundle","config file to generate MacOSX bundle (installer)"),
("WindowsInstaller","config files to generate windows installer"),
("zipios++","source of zipios++ lib")
]