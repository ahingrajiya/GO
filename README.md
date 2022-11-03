# GO
This code is to run on the CMSSW 12_5_0. To run this code follow the instructions below :

To compile CMSSW 12_5_0 to analyze miniAOD run the following commands:
`cmsrel CMSSW_12_5_0` <br />
`cd CMSSW_!2_5_0/src` <br />
`cmsenv` <br /> 
`scram build -j8` <br/>
`mkdir Demo` <br />
`cd Demo` <br />
`mkedanlzr DemoAnalyzer` <br />
`scram b` <br />

Copy the `ConfFile_cfg_miniAODselec.py` in the `python` folder inside the `Demo` directory. Copy `BuildFile.xml` and `DemoAnalyzer_miniAOD.cc` file to `plugins` folder in the `Demo` directory. <br />

Now go to `python` folder.
Run the code with following commmand <br />
`cmsRel ConfFile_cfg_miniAODselec.py`


To compile CMSSW 12_5_0 to analyze AOD run the following commands:
`cmsrel CMSSW_12_5_0` <br />
`cd CMSSW_!2_5_0/src` <br />
`cmsenv` <br /> 
`git cms-merge-topic CmsHI:forest_CMSSW_12_5_0` <br />
`git remote add cmshi git@github.com:CmsHI/cmssw.git` <br />
`scram build -j8` <br />
`mkdir Demo` <br />
`cd Demo` <br />
`mkedanlzr DemoAnalyzer` <br />
`scram b` <br />

Copy the `ConfFile_cfg_AOD.py` in the `python` folder inside the `Demo` directory. Copy `BuildFile.xml` and `DemoAnalyzer_AOD.cc` file to `plugins` folder in the `Demo` directory. <br />

Now go to `python` folder.
Run the code with following commmand <br />
`cmsRel ConfFile_cfg_AOD.py`
