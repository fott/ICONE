This folder contains various modules to perform simulations and post-processing of calculations for the ICONE project.

# <openmc_archiving.py>
The module provides 2 key procedures
* archDir=createArchiveDirectory() # this creates a new folder "./run_date_time" in the working script directory
* createArchivedDataset(archDir,statepoint=sp_filename, script="modules_testing_V1.ipynb", comment="essai n°3", source="Neutron 25MeV", geometry="Baseline_V1", geometryPara={'e0':26} 
this saves all the key information (data and input info) about the simulations into the archDir directory.
The archived directory contains the model.xml file, all the output files, the script used to perform the simulation and a <configuration.json> file with details of the simulation parameters (geometry and source in particular)
* Comment : The directory creation and the actually archiving of the files are split to avoid problems (the directory is created before saving things into it)
Things might be merged into a single command (but this is not much gain)

