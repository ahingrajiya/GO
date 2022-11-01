import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process('Demo',eras.Run3_pp_on_PbPb)

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load("CondCore.CondDB.CondDB_cfi")
process.load('Configuration.EventContent.EventContent_cff')

#process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

#process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
#process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")

#process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
#process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')

#process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

# Limit the output messages
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 500

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
)

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
				#'file:/eos/cms/store/group/phys_heavyions/mnguyen/miniAOD/D993B187-FDC6-CB44-991F-CA023BDEEC00.root'
				# 'file:/afs/cern.ch/work/d/ddesouza/GO_2021/make_my_miniAOD/CMSSW_11_2_0_pre10/src/AOD.root'
				'file:/eos/cms/store/group/phys_heavyions_ops/GO2022/AOD/MC_AOD_0.root'

#		'file:/afs/cern.ch/user/d/ddesouza/public/ForJaeBeom/004478C3-5C4E-4140-BE3B-E10FB965EFDF.root'
#            'file:/afs/cern.ch/work/d/ddesouza/tracking/CMSSW_10_3_3_patch1/src/HITrackingStudies/HITrackingStudies/test/step2_RAW2DIGI_L1Reco_RECO_3959.root'
#		'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/0041DCBB-C8E2-714D-B643-80AC8ABAE248.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/027D696D-B157-9941-B8F3-DB88FF908232.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/045FD64B-3109-E64F-8CEB-0F4ACA4CE2C5.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/0A0AAE7B-77A3-4446-8DBC-7A4B4C34D727.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/01CBBF53-4A10-AF47-B548-3801133C6AEB.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/02F97BF2-8AC2-DE4D-B578-796A1CA4C6EB.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/056A5BF1-5BD6-E443-A8B8-039F68A976D6.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/0274C28F-BAA2-4340-AAF7-B7B9229E1001.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/044E7A0B-C49B-6F4C-9452-1C63B2CC6B97.root',
#                'file:/eos/cms/store/group/phys_heavyions/caber/MiniAODValidation/AODfiles/05E0ACFC-BDBB-A041-891E-8E77E8F9C57C.root',
                ),
                skipBadFiles=cms.untracked.bool(True),
				duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
                            )

#define number of events to be processed (-1 means all)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Set the global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = cms.string('auto:phase1_2018_realistic_hi')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic_hi', '')
#process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

# Add PbPb centrality
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')
process.hiCentrality.produceHFhits = False
process.hiCentrality.produceHFtowers = False
process.hiCentrality.produceEcalhits = False
process.hiCentrality.produceZDChits = False
process.hiCentrality.produceETmidRapidity = False
process.hiCentrality.producePixelhits = False
process.hiCentrality.produceTracks = False
process.hiCentrality.producePixelTracks = False
process.hiCentrality.reUseCentrality = True
process.hiCentrality.srcReUse = cms.InputTag("hiCentrality","","reRECO")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("")
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
#        tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5F_v1032x02_mc"),#,"CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        label = cms.untracked.string("HFtowers")
        ),
    ])
process.cent_seq = cms.Sequence(process.hiCentrality * process.centralityBin)


# Add PbPb collision event selection
process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')


# Define the event selection sequence
process.eventFilter_HM = cms.Sequence(
    # process.offlinePrimaryVerticesRecovery 
#    process.hfCoincFilter2Th4 *
    # process.primaryVertexFilter *
    # process.clusterCompatibilityFilter
)


# Define the output

process.TFileService = cms.Service("TFileService",fileName = cms.string('PbPb_trk_AOD_noPFcut_0.root'))

process.demo = cms.EDAnalyzer('DemoAnalyzer',
                        # vertexCollection  = cms.InputTag("offlinePrimaryVerticesRecovery"),#"offlinePrimaryVertices"),
                        tracks   = cms.InputTag("generalTracks"),
                        CentralitySrc    = cms.InputTag("hiCentrality","","reRECO"),
                        CentralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
			towerSrc       = cms.InputTag("towerMaker"),
			pfSrc	       = cms.InputTag("particleFlow")
)

process.p = cms.Path(process.cent_seq*process.eventFilter_HM*process.demo)
process.schedule = cms.Schedule(process.p)

# peripheral pv recovery 
from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
# process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
# process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"
                                                                                  
