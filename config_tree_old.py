_treefilename = "/project/etp2/SUSYWh/NEW/Ntuples_HF/SignalPoints1603.root"

config = {
    "treeprocesses" : [
        ("300,150", [
            (_treefilename, "C1N2_Wh_hall_300p0_150p0_NoSys"),
        ]),
        ("500,250", [
            (_treefilename, "C1N2_Wh_hall_500p0_250p0_NoSys"),
        ]),
        ("700,0", [
            (_treefilename, "C1N2_Wh_hall_700p0_0p0_NoSys"),
        ]),
        ("800,0", [
            (_treefilename, "C1N2_Wh_hall_800p0_0p0_NoSys"),
        ]),
    ],
    "cutFlows" : {
        "cutflow_old" : [
            ("Preselection 1 lepton, $E_\mathrm{T}^\mathrm{miss} > $ 100 GeV, $N_\mathrm{jet30} =$ 2-3, $m_{\mathrm{T}}$ $>$ 50 GeV", "trigMatch_metTrig&&met>100&&nJet30>=2&&nJet30<4&&nLep_base==1&&nLep_signal==1&&mt>50"),
            ("$N_{\mathrm{b-jets,30}} =$ 2", "nBJet30_MV2c10==2"),
            ("$m_{\mathrm{bb}}$ $>$ 50 GeV", "mbb>50"),
            ("105 $<$ $m_{\mathrm{bb}}$ $<$ 135 GeV", "mbb>105&&mbb<135"),
            ("$m_{\mathrm{CT}}$ $>$ 160 GeV", "mct2>160"),
            ("$E_\mathrm{T}^\mathrm{miss} > $ 200 GeV", "met>200"),
        ],
        "cutflow_old_lmsr" : [
            ("100 $<$ $m_{\mathrm{T}}$ $<$ 140 GeV", "mt>100&&mt<140&&mct2>160&&trigMatch_metTrig&&met>200&&nJet30>=2&&nJet30<4&&nLep_base==1&&nLep_signal==1&&mt>50&&nBJet30_MV2c10==2&&mbb>105&&mbb<135")
        ],
        "cutflow_old_mmsr" : [
            ("140 $<$ $m_{\mathrm{T}}$ $<$ 200 GeV", "mt>140&&mt<200&&mct2>160&&trigMatch_metTrig&&met>200&&nJet30>=2&&nJet30<4&&nLep_base==1&&nLep_signal==1&&mt>50&&nBJet30_MV2c10==2&&mbb>105&&mbb<135")
        ],
        "cutflow_old_hmsr" : [
            ("$m_{\mathrm{T}}$ $>$ 200 GeV", "mt>200&&mct2>160&&trigMatch_metTrig&&met>200&&nJet30>=2&&nJet30<4&&nLep_base==1&&nLep_signal==1&&mt>50&&nBJet30_MV2c10==2&&mbb>105&&mbb<135")
        ]
    },
    "lumifactor" : 36100, # multiply the cutflows by this factor
    "format" : "tex",
    "outputdir" : "tex",
    "weights" : "genWeight*eventWeight*pileupWeight*leptonWeight*bTagWeight*0.58",
}
