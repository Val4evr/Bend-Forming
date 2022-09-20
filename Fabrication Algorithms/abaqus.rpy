# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-09.50.37 167380
# Run by harsh on Mon Aug 15 13:05:26 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.11979, 1.1169), width=164.833, 
    height=110.796)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile(
    'C:/Users/harsh/Documents/Wire Bending/Accuracy Model/AbaqusFiles/Code/FixedDisplacements/AbaqusFixedDisplacements_Standard_TetraTruss.py', 
    __main__.__dict__)
#: The model database has been saved to "C:\Users\harsh\Documents\Wire Bending\Accuracy Model\AbaqusFiles\TrussAlignDispStandard.cae".
#: Model: C:/Users/harsh/Documents/Wire Bending/Accuracy Model/AbaqusFiles/TrussAlignDispStandard.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          95
#: Number of Steps:              2
print 'RT script done'
#: RT script done
