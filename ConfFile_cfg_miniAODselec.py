import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process('Demo',eras.Run3_pp_on_PbPb)

process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# Limit the output messages
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 500

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
)

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
                #'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/MiniAODfiles/step2_HIMiniAOD.root',
		# 'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/miniAOD/MC_miniAOD_0.root',
                # 'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/miniAOD/MC_miniAOD_1.root',
                # 'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/miniAOD/MC_miniAOD_2.root',
                # 'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/miniAOD/MC_miniAOD_4.root',
                'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/miniAOD/MC_miniAOD_5.root'
                ),
                skipBadFiles=cms.untracked.bool(True),
				duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
                            )

#define number of events to be processed (-1 means all)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Set the global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic_hi', '')

# Add PbPb centrality
#process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
#process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')
#process.hiCentrality.produceHFhits = False
#process.hiCentrality.produceHFtowers = False
#process.hiCentrality.produceEcalhits = False
#process.hiCentrality.produceZDChits = False
#process.hiCentrality.produceETmidRapidity = False
#process.hiCentrality.producePixelhits = False
#process.hiCentrality.produceTracks = False
#process.hiCentrality.producePixelTracks = False
#process.hiCentrality.reUseCentrality = True
#process.hiCentrality.srcReUse = cms.InputTag("hiCentrality","","reRECO")
#process.centralityBin.Centrality = cms.InputTag("hiCentrality")
#process.centralityBin.centralityVariable = cms.string("HFtowers")
#process.centralityBin.nonDefaultGlauberModel = cms.string("")
#process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
#process.GlobalTag.toGet.extend([
#    cms.PSet(record = cms.string("HeavyIonRcd"),
##        tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5F_v1032x02_mc"),#,"CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
#        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
#        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#        label = cms.untracked.string("HFtowers")
#        ),
#    ])
#process.cent_seq = cms.Sequence(process.hiCentrality * process.centralityBin)


# Add PbPb collision event selection
# process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
# process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')

# Define the event selection sequence
process.eventFilter_HM = cms.Sequence(
#    process.phfCoincFilter2Th4 *
#    process.primaryVertexFilter *
#    process.clusterCompatibilityFilter
)


# Define the output

process.TFileService = cms.Service("TFileService",fileName = cms.string('PbPb_trk_miniAOD_withevselec_5.root'))

process.demo = cms.EDAnalyzer('DemoAnalyzer',
                        vertexCollection  = cms.InputTag("offlineSlimmedPrimaryVerticesRecovery"),#"offlinePrimaryVertices"),
                        tracks   = cms.InputTag("packedPFCandidates"),
                        chi2src = cms.InputTag("packedPFCandidateTrackChi2"),
			HFfilters = cms.InputTag("hiHFfilters","hiHFfilters","PAT"),
                        CentralitySrc    = cms.InputTag("hiCentrality","","reRECO"),
                        CentralityBinSrc = cms.InputTag("centralityBin","HFtowers")
)

process.p = cms.Path(process.eventFilter_HM*process.demo) # with selection
#process.p = cms.Path(process.demo) #no selection
process.schedule = cms.Schedule(process.p)

# peripheral pv recovery 
#from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
#process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
#process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"
                                                                                  
