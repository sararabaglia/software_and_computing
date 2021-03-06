from ROOT import *
from array import *
import os
from math import *
from pprint import pprint

#decide if you want run the whole program or you want run a demonstration
print("Do you want run the whole program or the demonstartion?")
print("(push 1 for the whole program or 2 for demonstation)")

run = raw_input()

#there is a control if the user push the wrong button
while (run != '1' and run != '2'):
 print("(push 1 for the whole program or 2 for demonstation)")
 run = raw_input()

#Definition for the whole program
if (run == '1'):
 
 #some controls to avoid that the program fails
 print("WARNING: if you want run the whole program you have to be inside the ATLAS-T3")
 print("Do you want continue? [y/n]")
 answer = raw_input()
 
 while (answer != 'y' and answer != 'n'):
  print("Do you want continue? [y/n]")
  answer = raw_input()
  
 if (answer == 'n'):
  print("Do you want run the demonstration? [y/n]")
  answer_2 = raw_input()
  
  while (answer_2 != 'y' and answer_2 != 'n'):
   print("Do you want run the demonstration? [y/n]")
   answer_2 = raw_input()
   
  if (answer_2 == 'y'):
   run = '2'
  if (answer_2 == 'n'):
   exit()
 
 if (answer == 'y'):
 
  #take the file root for the signal
  myfile = TFile('/home/ATLAS-T3/student-26/software_and_computing/allTrees_signal_NoSys.root')

  #study three different hypothesis for the masses of supersymmetric particles produced, each hypothesis is contained inside a tree of the input Roor file
  signal_tree = [myfile.Get('C1N2_WZ_300_0_NoSys'), myfile.Get('C1N2_WZ_500_100_NoSys'), myfile.Get('C1N2_WZ_1200_200_NoSys')]
 
  signal_entries = [0,0,0]

  #take the file root for the background
  myfile2 = TFile('/home/ATLAS-T3/student-26/software_and_computing/allTrees_bkg_NoSys.root')

  #in the root file for the background there are nine different types of background, one in each tree
  background_tree = [myfile2.Get('diboson_NoSys'),
                    myfile2.Get('multiboson_NoSys'),
                    myfile2.Get('singletop_NoSys'),
                    myfile2.Get('ttbar_NoSys'),
                    myfile2.Get('tth_NoSys'),
                    myfile2.Get('ttv_NoSys'),
                    myfile2.Get('vh_NoSys'),
                    myfile2.Get('wjets_NoSys'),
                    myfile2.Get('zjets_NoSys')]
 
  background_entries = [0,0,0,0,0,0,0,0,0]
 
  #definition of signal and background type
  signal_name = ["WZ (300,0)", "WZ (500,100)", "WZ (1200,200)"]
  background_name = ["Diboson", "Multiboson", "Single-top", "ttbar", "ttbarH", "ttbarV", "vh", "Wjets", "Zjets"]
 
  #set to zero the four matricies of counter, each element represents the counter after each cut. 
  #inside each elements there is the name of the cut and after that there are three number that are the counter for each signal trees that I consider for my analysis
  signal_counter = [["Preselection Cut",0,0,0],
                    ["Cut 1 (Nlep=1)",0,0,0],
                    ["Cut 2 (pT>25)",0,0,0],
                    ["Cut 3 (Njet(pT>30)=2-3)",0,0,0],
                    ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0],
                    ["Cut 5 (MET>200)",0,0,0],
                    ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0],
                    ["Cut 7 (70<mjj<105)",0,0,0],
                    ["Cut 8 (Nlarge-Rjet=0)",0,0,0],
                    ["Cut 9a (200<mT<380)",0,0,0],
                    ["Cut 9b (mT>380)",0,0,0]]

  #counter for the signal tree with a weight for each events
  signal_counter_weighed = [["Preselection Cut",0,0,0],
                            ["Cut 1 (Nlep=1)",0,0,0],
                            ["Cut 2 (pT>25)",0,0,0],
                            ["Cut 3 (Njet(pT>30)=2-3)",0,0,0],
                            ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0],
                            ["Cut 5 (MET>200)",0,0,0],
                            ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0],
                            ["Cut 7 (70<mjj<105)",0,0,0],
                            ["Cut 8 (Nlarge-Rjet=0)",0,0,0],
                            ["Cut 9a (200<mT<380)",0,0,0],
                            ["Cut 9b (mT>380)",0,0,0]]

  #inside each elements there is the name of the cut and after that there are nine number that are the counter for each background trees that I consider for my analysis
  bkg_counter = [["Preselection Cut",0,0,0,0,0,0,0,0,0],
                 ["Cut 1 (Nlep=1)",0,0,0,0,0,0,0,0,0],
                 ["Cut 2 (pT>25)",0,0,0,0,0,0,0,0,0],
                 ["Cut 3 (Njet(pT>30)=2-3)",0,0,0,0,0,0,0,0,0],
                 ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0,0,0,0,0,0,0],
                 ["Cut 5 (MET>200)",0,0,0,0,0,0,0,0,0],
                 ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0,0,0,0,0,0,0],
                 ["Cut 7 (70<mjj<105)",0,0,0,0,0,0,0,0,0],
                 ["Cut 8 (Nlarge-Rjet=0)",0,0,0,0,0,0,0,0,0],
                 ["Cut 9a (200<mT<380)",0,0,0,0,0,0,0,0,0],
                 ["Cut 9b (mT>380)",0,0,0,0,0,0,0,0,0]]

  #counter for the background tree with a weight for each events
  bkg_counter_weighed = [["Preselection Cut",0,0,0,0,0,0,0,0,0],
                         ["Cut 1 (Nlep=1)",0,0,0,0,0,0,0,0,0],
                         ["Cut 2 (pT>25)",0,0,0,0,0,0,0,0,0],
                         ["Cut 3 (Njet(pT>30)=2-3)",0,0,0,0,0,0,0,0,0],
                         ["Cut 4 (Nb-jet(pT>30)=0)",0,0,0,0,0,0,0,0,0],
                         ["Cut 5 (MET>200)",0,0,0,0,0,0,0,0,0],
                         ["Cut 6 (Delta_phi(l,met)<2.8)",0,0,0,0,0,0,0,0,0],
                         ["Cut 7 (70<mjj<105)",0,0,0,0,0,0,0,0,0],
                         ["Cut 8 (Nlarge-Rjet=0)",0,0,0,0,0,0,0,0,0],
                         ["Cut 9a (200<mT<380)",0,0,0,0,0,0,0,0,0],
                         ["Cut 9b (mT>380)",0,0,0,0,0,0,0,0,0]]



#Definition for DEMONSTRATION
if (run == '2'):
 print ("WARNING: if you want run the demonstration you must have the root files signal_Demo.root and bkg2_Demo.root inside your directory")
 print ("Do you want continue? [y/n]")
 
 answer_3 = raw_input()
 
 while (answer_3 != 'y' and answer_3 != 'n'):
  print("Do you want continue? [y/n]")
  answer_3 = raw_input()
 
 if (answer_3 == 'n'):
  exit()
 
 #take the file root for the signal demonstration
 myfile = TFile('signal_Demo.root')

 #in the dimonstration only one hypthesis for the masses of supersymmetric particles is studied
 signal_tree = [myfile.Get('C1N2_WZ_300_0_NoSys')]
 
 signal_entries = [0]
 #take the file root for the background demonstration
 myfile2 = TFile('bkg2_Demo.root')
 
 background_entries = [0]

 #in the dimonstration only one type of background is studied
 background_tree = [myfile2.Get('multiboson_NoSys')]
 
 #definition of signal and background type
 signal_name = ["WZ (300,0)"]
 background_name = ["Multiboson"]



 #set to zero the four matricies of counter for demonstration, each element represents the counter after each cut. 
 signal_counter = [["Preselection Cut",0],
                   ["Cut 1 (Nlep=1)",0],
                   ["Cut 2 (pT>25)",0],
                   ["Cut 3 (Njet(pT>30)=2-3)",0],
                   ["Cut 4 (Nb-jet(pT>30)=0)",0],
                   ["Cut 5 (MET>200)",0],
                   ["Cut 6 (Delta_phi(l,met)<2.8)",0],
                   ["Cut 7 (70<mjj<105)",0],
                   ["Cut 8 (Nlarge-Rjet=0)",0],
                   ["Cut 9a (200<mT<380)",0],
                   ["Cut 9b (mT>380)",0]]

 signal_counter_weighed = [["Preselection Cut",0],
                           ["Cut 1 (Nlep=1)",0],
                           ["Cut 2 (pT>25)",0],
                           ["Cut 3 (Njet(pT>30)=2-3)",0],
                           ["Cut 4 (Nb-jet(pT>30)=0)",0],
                           ["Cut 5 (MET>200)",0],
                           ["Cut 6 (Delta_phi(l,met)<2.8)",0],
                           ["Cut 7 (70<mjj<105)",0],
                           ["Cut 8 (Nlarge-Rjet=0)",0],
                           ["Cut 9a (200<mT<380)",0],
                           ["Cut 9b (mT>380)",0]]

 bkg_counter = [["Preselection Cut",0],
                ["Cut 1 (Nlep=1)",0],
                ["Cut 2 (pT>25)",0],
                ["Cut 3 (Njet(pT>30)=2-3)",0],
                ["Cut 4 (Nb-jet(pT>30)=0)",0],
                ["Cut 5 (MET>200)",0],
                ["Cut 6 (Delta_phi(l,met)<2.8)",0],
                ["Cut 7 (70<mjj<105)",0],
                ["Cut 8 (Nlarge-Rjet=0)",0],
                ["Cut 9a (200<mT<380)",0],
                ["Cut 9b (mT>380)",0]]

 bkg_counter_weighed = [["Preselection Cut",0],
                        ["Cut 1 (Nlep=1)",0],
                        ["Cut 2 (pT>25)",0],
                        ["Cut 3 (Njet(pT>30)=2-3)",0],
                        ["Cut 4 (Nb-jet(pT>30)=0)",0],
                        ["Cut 5 (MET>200)",0],
                        ["Cut 6 (Delta_phi(l,met)<2.8)",0],
                        ["Cut 7 (70<mjj<105)",0],
                        ["Cut 8 (Nlarge-Rjet=0)",0],
                        ["Cut 9a (200<mT<380)",0],
                        ["Cut 9b (mT>380)",0]]



#total number of events in each signal tree
for i in range(0, len(signal_tree)):
 signal_entries[i] = signal_tree[i].GetEntries()

#total number of events in each background trees
for i in range(0,len(background_tree)):
 background_entries[i] = background_tree[i].GetEntriesFast()


#start cut flow for signal

for tree_number in range(0,len(signal_tree)):
 for j_entry in range(signal_entries[tree_number]):
  signal_tree[tree_number].GetEvent(j_entry)
  weight = getattr(signal_tree[tree_number], "genWeight")*getattr(signal_tree[tree_number], "pileupWeight")*getattr(signal_tree[tree_number], "eventWeight")*getattr(signal_tree[tree_number], "leptonWeight")*getattr(signal_tree[tree_number], "bTagWeight")
  if (getattr(signal_tree[tree_number], "met")>200
      and getattr(signal_tree[tree_number], "nJet30")>=1
      and getattr(signal_tree[tree_number], "nLep_base")==1
      and getattr(signal_tree[tree_number], "nLep_signal")==1
      and getattr(signal_tree[tree_number], "mt")>50):
   signal_counter[0][tree_number+1] = signal_counter[0][tree_number+1] + 1
   signal_counter_weighed[0][tree_number+1] = signal_counter_weighed[0][tree_number+1] + weight
  else: continue
    
  if (getattr(signal_tree[tree_number], "nLep_base")==1
      and getattr(signal_tree[tree_number], "nLep_signal")==1):
   signal_counter[1][tree_number+1] = signal_counter[1][tree_number+1] + 1
   signal_counter_weighed[1][tree_number+1] = signal_counter_weighed[1][tree_number+1] + weight
  else: continue
    
  if getattr(signal_tree[tree_number], "lep1Pt")>25:
   signal_counter[2][tree_number+1] = signal_counter[2][tree_number+1] + 1
   signal_counter_weighed[2][tree_number+1] = signal_counter_weighed[2][tree_number+1] + weight
  else: continue
    
  if (getattr(signal_tree[tree_number], "nJet30")==2
      or getattr(signal_tree[tree_number], "nJet30")==3):
   signal_counter[3][tree_number+1] = signal_counter[3][tree_number+1] + 1
   signal_counter_weighed[3][tree_number+1] = signal_counter_weighed[3][tree_number+1] + weight
  else: continue
    
  if getattr(signal_tree[tree_number], "nBJet30_DL1")==0:
   signal_counter[4][tree_number+1] = signal_counter[4][tree_number+1] + 1
   signal_counter_weighed[4][tree_number+1] = signal_counter_weighed[4][tree_number+1] + weight
  else: continue
    
  if getattr(signal_tree[tree_number], "met")>200:
   signal_counter[5][tree_number+1] = signal_counter[5][tree_number+1] + 1
   signal_counter_weighed[5][tree_number+1] = signal_counter_weighed[5][tree_number+1] + weight
  else: continue
    
  if getattr(signal_tree[tree_number], "met_Phi")<2.8:
   signal_counter[6][tree_number+1] = signal_counter[6][tree_number+1] + 1
   signal_counter_weighed[6][tree_number+1] = signal_counter_weighed[6][tree_number+1] + weight
  else: continue
  
  jet1_pt = getattr(signal_tree[tree_number], "jet1Pt")
  jet1_Eta = getattr(signal_tree[tree_number], "jet1Eta")
  jet1_Phi = getattr(signal_tree[tree_number], "jet1Phi")
  jet2_pt = getattr(signal_tree[tree_number], "jet2Pt")
  jet2_Eta = getattr(signal_tree[tree_number], "jet2Eta")
  jet2_Phi = getattr(signal_tree[tree_number], "jet2Phi")
  mjj = sqrt(2*jet1_pt*jet2_pt*(cosh(jet1_Eta-jet2_Eta)-cos(jet1_Phi-jet2_Phi)))
  if (mjj<105
      and mjj>70):
   signal_counter[7][tree_number+1] = signal_counter[7][tree_number+1] + 1
   signal_counter_weighed[7][tree_number+1] = signal_counter_weighed[7][tree_number+1] + weight
  else: continue
  
  if getattr(signal_tree[tree_number], "nFatjets")==0:
   signal_counter[8][tree_number+1] = signal_counter[8][tree_number+1] + 1
   signal_counter_weighed[8][tree_number+1] = signal_counter_weighed[8][tree_number+1] + weight
  else: continue
  
  if (getattr(signal_tree[tree_number], "mt")>200
      and getattr(signal_tree[tree_number], "mt")<380):
   signal_counter[9][tree_number+1] = signal_counter[9][tree_number+1] + 1
   signal_counter_weighed[9][tree_number+1] = signal_counter_weighed[9][tree_number+1] + weight
  
  if getattr(signal_tree[tree_number], "mt")>380:
   signal_counter[10][tree_number+1] = signal_counter[10][tree_number+1] + 1
   signal_counter_weighed[10][tree_number+1] = signal_counter_weighed[10][tree_number+1] + weight
  else: continue

#end cut flow for the signal

#start cut flow for the background

for bkg_type in range(0,len(background_tree)):
 for i_entry in range(background_entries[bkg_type]):
  background_tree[bkg_type].GetEvent(i_entry)
  weight = getattr(background_tree[bkg_type], "genWeight")*getattr(background_tree[bkg_type], "pileupWeight")*getattr(background_tree[bkg_type], "eventWeight")*getattr(background_tree[bkg_type], "leptonWeight")*getattr(background_tree[bkg_type], "bTagWeight")
  if (getattr(background_tree[bkg_type], "met")>200
      and getattr(background_tree[bkg_type], "nJet30")>=1
      and getattr(background_tree[bkg_type], "nLep_base")==1
      and getattr(background_tree[bkg_type], "nLep_signal")==1
      and getattr(background_tree[bkg_type], "mt")>50):
    bkg_counter[0][bkg_type+1] = bkg_counter[0][bkg_type+1] + 1
    bkg_counter_weighed[0][bkg_type+1] = bkg_counter_weighed[0][bkg_type+1] + weight
  else: continue
  if (getattr(background_tree[bkg_type], "nLep_base")==1
      and getattr(background_tree[bkg_type], "nLep_signal")==1):
    bkg_counter[1][bkg_type+1] = bkg_counter[1][bkg_type+1] + 1
    bkg_counter_weighed[1][bkg_type+1] = bkg_counter_weighed[1][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "lep1Pt")>25:
    bkg_counter[2][bkg_type+1] = bkg_counter[2][bkg_type+1] + 1
    bkg_counter_weighed[2][bkg_type+1] = bkg_counter_weighed[2][bkg_type+1] + weight
  else: continue
    
  if (getattr(background_tree[bkg_type], "nJet30")==2
      or getattr(background_tree[bkg_type], "nJet30")==3):
   bkg_counter[3][bkg_type+1] = bkg_counter[3][bkg_type+1] + 1
   bkg_counter_weighed[3][bkg_type+1] = bkg_counter_weighed[3][bkg_type+1] + weight 
  else: continue
    
  if getattr(background_tree[bkg_type], "nBJet30_DL1")==0:
    bkg_counter[4][bkg_type+1] = bkg_counter[4][bkg_type+1] + 1
    bkg_counter_weighed[4][bkg_type+1] = bkg_counter_weighed[4][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "met")>200:
    bkg_counter[5][bkg_type+1] = bkg_counter[5][bkg_type+1] + 1
    bkg_counter_weighed[5][bkg_type+1] = bkg_counter_weighed[5][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "met_Phi")<2.8:
    bkg_counter[6][bkg_type+1] = bkg_counter[6][bkg_type+1] + 1
    bkg_counter_weighed[6][bkg_type+1] = bkg_counter_weighed[6][bkg_type+1] + weight
  else: continue
  
  jet1_pt = getattr(background_tree[bkg_type], "jet1Pt")
  jet1_Eta = getattr(background_tree[bkg_type], "jet1Eta")
  jet1_Phi = getattr(background_tree[bkg_type], "jet1Phi")
  jet2_pt = getattr(background_tree[bkg_type], "jet2Pt")
  jet2_Eta = getattr(background_tree[bkg_type], "jet2Eta")
  jet2_Phi = getattr(background_tree[bkg_type], "jet2Phi")
  mjj = sqrt(2*jet1_pt*jet2_pt*(cosh(jet1_Eta-jet2_Eta)-cos(jet1_Phi-jet2_Phi)))
  if (mjj<105
      and mjj>70):
    bkg_counter[7][bkg_type+1] = bkg_counter[7][bkg_type+1] + 1
    bkg_counter_weighed[7][bkg_type+1] = bkg_counter_weighed[7][bkg_type+1] + weight
  else: continue
    
  if getattr(background_tree[bkg_type], "nFatjets")==0:
    bkg_counter[8][bkg_type+1] = bkg_counter[8][bkg_type+1] + 1
    bkg_counter_weighed[8][bkg_type+1] = bkg_counter_weighed[8][bkg_type+1] + weight
  else: continue
    
  if (getattr(background_tree[bkg_type], "mt")>200
      and getattr(background_tree[bkg_type], "mt")<380):
    bkg_counter[9][bkg_type+1] = bkg_counter[9][bkg_type+1] + 1
    bkg_counter_weighed[9][bkg_type+1] = bkg_counter_weighed[9][bkg_type+1] + weight
    
  if getattr(background_tree[bkg_type], "mt")>380:
    bkg_counter[10][bkg_type+1] = bkg_counter[10][bkg_type+1] + 1
    bkg_counter_weighed[10][bkg_type+1] = bkg_counter_weighed[10][bkg_type+1] + weight
  else: continue

#end cut flow for the background

#computation of signal over the background (S/B)
total_bkg = 0
total_weighed_bkg = 0

for v in range (0,len(background_tree)):
 total_bkg = total_bkg + bkg_counter[9][v+1]
 total_weighed_bkg = total_weighed_bkg + bkg_counter_weighed[9][v+1]

if (run == '1'):
 signal_over_bkg = [0,0,0]
 signal_over_bkg_weighed = [0,0,0]

if (run == '2'):
 signal_over_bkg = [0]
 signal_over_bkg_weighed = [0]


for z in range (0,len(signal_tree)):
  signal_over_bkg[z] = float(signal_counter[9][z+1])/float(total_bkg)

for x in range (0,len(signal_tree)):
  signal_over_bkg_weighed[x] = signal_counter_weighed[9][x+1]/total_weighed_bkg

#print the result of the cut flow in a txt file
if (run == '1'):
 f = open("cut_result.txt", "w")

if (run == '2'):
 f = open("Demo_cut_result.txt", "w")

f.write("                   ")

for q in signal_name:
  f.write(q)
  f.write("  ")

f.write('\n')

for a in signal_counter:
  for b in a:
    f.write(str(b))
    f.write(" ")
  f.write('\n')
  
f.write('\n')

for c in signal_counter_weighed:
  for d in c:
    f.write(str(d))
    f.write(" ")
  f.write('\n')
  
f.write('\n')

for e in bkg_counter:
  for m in e:
    f.write(str(m))
    f.write(" ")
  f.write('\n')
  
f.write('\n')

for g in bkg_counter_weighed:
  for h in g:
    f.write(str(h))
    f.write(" ")
  f.write('\n')
  
f.write('\n')

for s in signal_over_bkg:
  i = 1
  f.write("S/B_")
  f.write(str(i))
  f.write(" = ")
  f.write(str(s))
  i = i + 1
  
f.write('\n')

for s in signal_over_bkg_weighed:
  i = 1
  f.write("S/B_weighed")
  f.write(str(i))
  f.write(" = ")
  f.write(str(s))
  i = i + 1

f.close()

