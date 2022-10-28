from argparse import ONE_OR_MORE
from opcode import stack_effect
from turtle import shapesize
import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.special import expit


st.set_page_config(layout="wide")
st.title("HELOC Risk Evaluation")

# preset demos
selected_demos = st.selectbox("Pick a demo", ("Empty", "Demo1", "Demo2", "Demo3"))

# Run botton
st.write("Press 'Run Model' button to run.")
run = st.button("Run Model")

# basic layout: 3 columns
# col1: sliders
# col2: input number
# col3: output
col1, col2 = st.columns([3,1])
col1.header("Input Panel")
col2.header("Output Panel")
col1, col2, col3 = st.columns(3)

# dicstionary storing slider and input box values
# "st.session_state object:" , st.session_state

# connection of slider and input
def update_ExternalRiskEstimate():
    st.session_state.ExternalRiskEstimate = st.session_state.ExternalRiskEstimate_slider    
def update_ExternalRiskEstimate_slider():
    st.session_state.ExternalRiskEstimate_slider = st.session_state.ExternalRiskEstimate 

def update_MSinceOldestTradeOpen():
    st.session_state.MSinceOldestTradeOpen = st.session_state.MSinceOldestTradeOpen_slider    
def update_MSinceOldestTradeOpen_slider():
    st.session_state.MSinceOldestTradeOpen_slider = st.session_state.MSinceOldestTradeOpen

def update_MSinceMostRecentTradeOpen():
    st.session_state.MSinceMostRecentTradeOpen = st.session_state.MSinceMostRecentTradeOpen_slider    
def update_MSinceMostRecentTradeOpen_slider():
    st.session_state.MSinceMostRecentTradeOpen_slider = st.session_state.MSinceMostRecentTradeOpen

def update_AverageMInFile():
    st.session_state.AverageMInFile = st.session_state.AverageMInFile_slider    
def update_AverageMInFile_slider():
    st.session_state.AverageMInFile_slider = st.session_state.AverageMInFile

def update_NumSatisfactoryTrades():
    st.session_state.NumSatisfactoryTrades = st.session_state.NumSatisfactoryTrades_slider    
def update_NumSatisfactoryTrades_slider():
    st.session_state.NumSatisfactoryTrades_slider = st.session_state.NumSatisfactoryTrades

def update_NumTrades60Ever2DerogPubRec():
    st.session_state.NumTrades60Ever2DerogPubRec = st.session_state.NumTrades60Ever2DerogPubRec_slider    
def update_NumTrades60Ever2DerogPubRec_slider():
    st.session_state.NumTrades60Ever2DerogPubRec_slider = st.session_state.NumTrades60Ever2DerogPubRec

def update_NumTrades90Ever2DerogPubRec():
    st.session_state.NumTrades90Ever2DerogPubRec = st.session_state.NumTrades90Ever2DerogPubRec_slider    
def update_NumTrades90Ever2DerogPubRec_slider():
    st.session_state.NumTrades90Ever2DerogPubRec_slider = st.session_state.NumTrades90Ever2DerogPubRec

def update_PercentTradesNeverDelq():
    st.session_state.PercentTradesNeverDelq = st.session_state.PercentTradesNeverDelq_slider    
def update_PercentTradesNeverDelq_slider():
    st.session_state.PercentTradesNeverDelq_slider = st.session_state.PercentTradesNeverDelq

def update_MSinceMostRecentDelq():
    st.session_state.MSinceMostRecentDelq = st.session_state.MSinceMostRecentDelq_slider    
def update_MSinceMostRecentDelq_slider():
    st.session_state.MSinceMostRecentDelq_slider = st.session_state.MSinceMostRecentDelq

def update_MaxDelq2PublicRecLast12M():
    st.session_state.MaxDelq2PublicRecLast12M = st.session_state.MaxDelq2PublicRecLast12M_slider    
def update_MaxDelq2PublicRecLast12M_slider():
    st.session_state.MaxDelq2PublicRecLast12M_slider = st.session_state.MaxDelq2PublicRecLast12M

def update_MaxDelqEver():
    st.session_state.MaxDelqEver = st.session_state.MaxDelqEver_slider    
def update_MaxDelqEver_slider():
    st.session_state.MaxDelqEver_slider = st.session_state.MaxDelqEver

def update_NumTotalTrades():
    st.session_state.NumTotalTrades = st.session_state.NumTotalTrades_slider    
def update_NumTotalTrades_slider():
    st.session_state.NumTotalTrades_slider = st.session_state.NumTotalTrades

def update_NumTradesOpeninLast12M():
    st.session_state.NumTradesOpeninLast12M = st.session_state.NumTradesOpeninLast12M_slider    
def update_NumTradesOpeninLast12M_slider():
    st.session_state.NumTradesOpeninLast12M_slider = st.session_state.NumTradesOpeninLast12M

def update_PercentInstallTrades():
    st.session_state.PercentInstallTrades = st.session_state.PercentInstallTrades_slider    
def update_PercentInstallTrades_slider():
    st.session_state.PercentInstallTrades_slider = st.session_state.PercentInstallTrades

def update_MSinceMostRecentInqexcl7days():
    st.session_state.MSinceMostRecentInqexcl7days = st.session_state.MSinceMostRecentInqexcl7days_slider    
def update_MSinceMostRecentInqexcl7days_slider():
    st.session_state.MSinceMostRecentInqexcl7days_slider = st.session_state.MSinceMostRecentInqexcl7days

def update_NumInqLast6M():
    st.session_state.NumInqLast6M = st.session_state.NumInqLast6M_slider    
def update_NumInqLast6M_slider():
    st.session_state.NumInqLast6M_slider = st.session_state.NumInqLast6M

def update_NumInqLast6Mexcl7days():
    st.session_state.NumInqLast6Mexcl7days = st.session_state.NumInqLast6Mexcl7days_slider    
def update_NumInqLast6Mexcl7days_slider():
    st.session_state.NumInqLast6Mexcl7days_slider = st.session_state.NumInqLast6Mexcl7days

def update_NetFractionRevolvingBurden():
    st.session_state.NetFractionRevolvingBurden = st.session_state.NetFractionRevolvingBurden_slider    
def update_NetFractionRevolvingBurden_slider():
    st.session_state.NetFractionRevolvingBurden_slider = st.session_state.NetFractionRevolvingBurden

def update_NetFractionInstallBurden():
    st.session_state.NetFractionInstallBurden = st.session_state.NetFractionInstallBurden_slider    
def update_NetFractionInstallBurden_slider():
    st.session_state.NetFractionInstallBurden_slider = st.session_state.NetFractionInstallBurden

def update_NumRevolvingTradesWBalance():
    st.session_state.NumRevolvingTradesWBalance = st.session_state.NumRevolvingTradesWBalance_slider    
def update_NumRevolvingTradesWBalance_slider():
    st.session_state.NumRevolvingTradesWBalance_slider = st.session_state.NumRevolvingTradesWBalance

def update_NumInstallTradesWBalance():
    st.session_state.NumInstallTradesWBalance = st.session_state.NumInstallTradesWBalance_slider    
def update_NumInstallTradesWBalance_slider():
    st.session_state.NumInstallTradesWBalance_slider = st.session_state.NumInstallTradesWBalance

def update_NumBank2NatlTradesWHighUtilization():
    st.session_state.NumBank2NatlTradesWHighUtilization = st.session_state.NumBank2NatlTradesWHighUtilization_slider    
def update_NumBank2NatlTradesWHighUtilization_slider():
    st.session_state.NumBank2NatlTradesWHighUtilization_slider = st.session_state.NumBank2NatlTradesWHighUtilization

def update_PercentTradesWBalance():
    st.session_state.PercentTradesWBalance = st.session_state.PercentTradesWBalance_slider    
def update_PercentTradesWBalance_slider():
    st.session_state.PercentTradesWBalance_slider = st.session_state.PercentTradesWBalance


# inputs
# col2.header("Input Panel")
col2.write("You may enter feature values directly")

ExternalRiskEstimate = col2.number_input('ExternalRiskEstimate(Decreasing)', -9, 100, 0, 1, key = "ExternalRiskEstimate", on_change = update_ExternalRiskEstimate_slider)
MSinceOldestTradeOpen = col2.number_input('MSinceOldestTradeOpen(Decreasing)', -9, 810, 0, 1, key = "MSinceOldestTradeOpen", on_change = update_MSinceOldestTradeOpen_slider)
MSinceMostRecentTradeOpen = col2.number_input('MSinceMostRecentTradeOpen(Decreasing)', -9, 400,0,1, key = "MSinceMostRecentTradeOpen", on_change = update_MSinceMostRecentTradeOpen_slider)
AverageMInFile = col2.number_input('AverageMInFile(Decreasing)', -9, 400,0,1, key = "AverageMInFile", on_change = update_AverageMInFile_slider)
NumSatisfactoryTrades = col2.number_input('NumSatisfactoryTrades(Decreasing)', -9, 80,0,1, key = "NumSatisfactoryTrades", on_change = update_NumSatisfactoryTrades_slider)
NumTrades60Ever2DerogPubRec = col2.number_input('NumTrades60Ever2DerogPubRec(Increasing)', -9, 20,0,1, key = "NumTrades60Ever2DerogPubRec", on_change = update_NumTrades60Ever2DerogPubRec_slider)
NumTrades90Ever2DerogPubRec = col2.number_input('NumTrades90Ever2DerogPubRec(Increasing)', -9, 20,0,1, key = "NumTrades90Ever2DerogPubRec", on_change = update_NumTrades90Ever2DerogPubRec_slider)
PercentTradesNeverDelq = col2.number_input('PercentTradesNeverDelq(Decreasing)', -9, 100,0,1, key = "PercentTradesNeverDelq", on_change = update_PercentTradesNeverDelq_slider)
MSinceMostRecentDelq = col2.number_input('MSinceMostRecentDelq(Decreasing)', -9, 90,0,1, key = "MSinceMostRecentDelq", on_change = update_MSinceMostRecentDelq_slider)
MaxDelq2PublicRecLast12M = col2.number_input('MaxDelq2PublicRecLast12M(Decreasing)', -9, 7,0,1, key = "MaxDelq2PublicRecLast12M", on_change = update_MaxDelq2PublicRecLast12M_slider)
MaxDelqEver = col2.number_input('MaxDelqEver(Decreasing)', -9, 5,0,1, key = "MaxDelqEver", on_change = update_MaxDelqEver_slider)
NumTotalTrades = col2.number_input('NumTotalTrades(No constraint)', -9, 110,0,1, key = "NumTotalTrades", on_change = update_NumTotalTrades_slider)
NumTradesOpeninLast12M = col2.number_input('NumTradesOpeninLast12M(Increasing)', -9, 20,0,1, key = "NumTradesOpeninLast12M", on_change = update_NumTradesOpeninLast12M_slider)
PercentInstallTrades = col2.number_input('PercentInstallTrades(No constraint)', -9, 100,0,1, key = "PercentInstallTrades", on_change = update_PercentInstallTrades_slider)
MSinceMostRecentInqexcl7days = col2.number_input('MSinceMostRecentInqexcl7days(Decreasing)', -9, 30,0,1, key = "MSinceMostRecentInqexcl7days", on_change = update_MSinceMostRecentInqexcl7days_slider)
NumInqLast6M = col2.number_input('NumInqLast6M(Increasing)', -9, 70,0,1, key = "NumInqLast6M", on_change = update_NumInqLast6M_slider)
NumInqLast6Mexcl7days = col2.number_input('NumInqLast6Mexcl7days(Increasing)', -9, 70,0,1, key = "NumInqLast6Mexcl7days", on_change = update_NumInqLast6Mexcl7days_slider)
NetFractionRevolvingBurden = col2.number_input('NetFractionRevolvingBurden(Increasing)', -9, 240,0,1, key = "NetFractionRevolvingBurden", on_change = update_NetFractionRevolvingBurden_slider)
NetFractionInstallBurden = col2.number_input('NetFractionInstallBurden(Increasing)', -9, 480,0,1, key = "NetFractionInstallBurden", on_change = update_NetFractionInstallBurden_slider)
NumRevolvingTradesWBalance = col2.number_input('NumRevolvingTradesWBalance(No constraint)', -9, 40,0,1, key = "NumRevolvingTradesWBalance", on_change = update_NumRevolvingTradesWBalance_slider)
NumInstallTradesWBalance = col2.number_input('NumInstallTradesWBalance(No constraint)', -9, 30,0,1, key = "NumInstallTradesWBalance", on_change = update_NumInstallTradesWBalance_slider)
NumBank2NatlTradesWHighUtilization = col2.number_input('NumBank2NatlTradesWHighUtilization(Increasing)', -9, 20,0,1, key = "NumBank2NatlTradesWHighUtilization", on_change = update_NumBank2NatlTradesWHighUtilization_slider)
PercentTradesWBalance = col2.number_input('PercentTradesWBalance(No constraint)', -9, 100,0,1, key = "PercentTradesWBalance", on_change = update_PercentTradesWBalance_slider)

# features sliders
# col1.header("Input Panel")
col1.write("Please set your feature values")

ExternalRiskEstimate_slider = col1.slider('ExternalRiskEstimate(Decreasing)', -9, 100, 0, 1, key = 'ExternalRiskEstimate_slider', on_change = update_ExternalRiskEstimate)
MSinceOldestTradeOpen_slider = col1.slider('MSinceOldestTradeOpen(Decreasing)', -9, 810, 0, 1, key = 'MSinceOldestTradeOpen_slider', on_change = update_MSinceOldestTradeOpen)
MSinceMostRecentTradeOpen_slider = col1.slider('MSinceMostRecentTradeOpen(Decreasing)', -9, 400,0,1, key = 'MSinceMostRecentTradeOpen_slider', on_change = update_MSinceMostRecentTradeOpen)
AverageMInFile_slider = col1.slider('AverageMInFile(Decreasing)', -9, 400,0,1, key = 'AverageMInFile_slider', on_change = update_AverageMInFile)
NumSatisfactoryTrades_slider = col1.slider('NumSatisfactoryTrades(Decreasing)', -9, 80,0,1, key = 'NumSatisfactoryTrades_slider', on_change = update_NumSatisfactoryTrades)
NumTrades60Ever2DerogPubRec_slider = col1.slider('NumTrades60Ever2DerogPubRec(Increasing)', -9, 20,0,1, key = 'NumTrades60Ever2DerogPubRec_slider', on_change = update_NumTrades60Ever2DerogPubRec)
NumTrades90Ever2DerogPubRec_slider = col1.slider('NumTrades90Ever2DerogPubRec(Increasing)', -9, 20,0,1, key = 'NumTrades90Ever2DerogPubRec_slider', on_change = update_NumTrades90Ever2DerogPubRec)
PercentTradesNeverDelq_slider = col1.slider('PercentTradesNeverDelq(Decreasing)', -9, 100,0,1, key = 'PercentTradesNeverDelq_slider', on_change = update_PercentTradesNeverDelq)
MSinceMostRecentDelq_slider = col1.slider('MSinceMostRecentDelq(Decreasing)', -9, 90,0,1, key = 'MSinceMostRecentDelq_slider', on_change = update_MSinceMostRecentDelq)
MaxDelq2PublicRecLast12M_slider = col1.slider('MaxDelq2PublicRecLast12M(Decreasing)', -9, 7,0,1, key = 'MaxDelq2PublicRecLast12M_slider', on_change = update_MaxDelq2PublicRecLast12M)
MaxDelqEver_slider = col1.slider('MaxDelqEver(Decreasing)', -9, 5,0,1, key = 'MaxDelqEver_slider', on_change = update_MaxDelqEver)
NumTotalTrades_slider = col1.slider('NumTotalTrades(No constraint)', -9, 110,0,1, key = 'NumTotalTrades_slider', on_change = update_NumTotalTrades)
NumTradesOpeninLast12M_slider = col1.slider('NumTradesOpeninLast12M(Increasing)', -9, 20,0,1, key = 'NumTradesOpeninLast12M_slider', on_change = update_NumTradesOpeninLast12M)
PercentInstallTrades_slider = col1.slider('PercentInstallTrades(No constraint)', -9, 100,0,1, key = 'PercentInstallTrades_slider', on_change = update_PercentInstallTrades)
MSinceMostRecentInqexcl7days_slider = col1.slider('MSinceMostRecentInqexcl7days(Decreasing)', -9, 30,0,1, key = 'MSinceMostRecentInqexcl7days_slider', on_change = update_MSinceMostRecentInqexcl7days)
NumInqLast6M_slider = col1.slider('NumInqLast6M(Increasing)', -9, 70,0,1, key = 'NumInqLast6M_slider', on_change = update_NumInqLast6M)
NumInqLast6Mexcl7days_slider = col1.slider('NumInqLast6Mexcl7days(Increasing)', -9, 70,0,1, key = 'NumInqLast6Mexcl7days_slider', on_change = update_NumInqLast6Mexcl7days)
NetFractionRevolvingBurden_slider = col1.slider('NetFractionRevolvingBurden(Increasing)', -9, 240,0,1, key = 'NetFractionRevolvingBurden_slider', on_change = update_NetFractionRevolvingBurden)
NetFractionInstallBurden_slider = col1.slider('NetFractionInstallBurden(Increasing)', -9, 480,0,1, key = 'NetFractionInstallBurden_slider', on_change = update_NetFractionInstallBurden)
NumRevolvingTradesWBalance_slider = col1.slider('NumRevolvingTradesWBalance(No constraint)', -9, 40,0,1, key = 'NumRevolvingTradesWBalance_slider', on_change = update_NumRevolvingTradesWBalance)
NumInstallTradesWBalance_slider = col1.slider('NumInstallTradesWBalance(No constraint)', -9, 30,0,1, key = 'NumInstallTradesWBalance_slider', on_change = update_NumInstallTradesWBalance)
NumBank2NatlTradesWHighUtilization_slider = col1.slider('NumBank2NatlTradesWHighUtilization(Increasing)', -9, 20,0,1, key = 'NumBank2NatlTradesWHighUtilization_slider', on_change = update_NumBank2NatlTradesWHighUtilization)
PercentTradesWBalance_slider = col1.slider('PercentTradesWBalance(No constraint)', -9, 100,0,1, key = 'PercentTradesWBalance_slider', on_change = update_PercentTradesWBalance)



# input model

if NumTotalTrades > 0:
    SatisfactoryTradesRate = NumSatisfactoryTrades/NumTotalTrades
else: SatisfactoryTradesRate = 0

model_Features = np.array([])
model_Features = np.append(model_Features, ExternalRiskEstimate)
model_Features = np.append(model_Features, MSinceOldestTradeOpen)
model_Features = np.append(model_Features, MSinceMostRecentTradeOpen)
model_Features = np.append(model_Features, AverageMInFile)
model_Features = np.append(model_Features, NumSatisfactoryTrades)
model_Features = np.append(model_Features, NumTrades60Ever2DerogPubRec)
model_Features = np.append(model_Features, NumTrades90Ever2DerogPubRec)
model_Features = np.append(model_Features, PercentTradesNeverDelq)
model_Features = np.append(model_Features, MSinceMostRecentInqexcl7days)
model_Features = np.append(model_Features, MaxDelq2PublicRecLast12M)
model_Features = np.append(model_Features, MaxDelqEver)
model_Features = np.append(model_Features, NumTotalTrades)
model_Features = np.append(model_Features, NumTradesOpeninLast12M)
model_Features = np.append(model_Features, PercentInstallTrades)
model_Features = np.append(model_Features, MSinceMostRecentInqexcl7days)
model_Features = np.append(model_Features, NumInqLast6M)
model_Features = np.append(model_Features, NumInqLast6Mexcl7days)
model_Features = np.append(model_Features, NetFractionRevolvingBurden)
model_Features = np.append(model_Features, NetFractionInstallBurden)
model_Features = np.append(model_Features, NumRevolvingTradesWBalance)
model_Features = np.append(model_Features, NumInstallTradesWBalance)
model_Features = np.append(model_Features, NumBank2NatlTradesWHighUtilization)
model_Features = np.append(model_Features, PercentTradesWBalance)
model_Features = np.append(model_Features, SatisfactoryTradesRate)

if MSinceMostRecentDelq == -7:
    MSinceMostRecentDelq_7 = 1
else: MSinceMostRecentDelq_7 = 0
model_Features = np.append(model_Features, MSinceMostRecentDelq_7)

if MSinceMostRecentInqexcl7days == -7:
    MMSinceMostRecentInqexcl7days_7 = 1
else: MMSinceMostRecentInqexcl7days_7 = 0
model_Features = np.append(model_Features, MMSinceMostRecentInqexcl7days_7)

if MSinceOldestTradeOpen == -8:
    MSinceOldestTradeOpen_8 = 1
else: MSinceOldestTradeOpen_8 = 0
model_Features = np.append(model_Features, MSinceOldestTradeOpen_8)

if MSinceMostRecentDelq == -8:
    MSinceMostRecentDelq_8 = 1
else: MSinceMostRecentDelq_8 = 0
model_Features = np.append(model_Features, MSinceMostRecentDelq_8)

if MSinceMostRecentInqexcl7days == -8:
    MSinceMostRecentInqexcl7days_8 = 1
else: MSinceMostRecentInqexcl7days_8 = 0
model_Features = np.append(model_Features, MSinceMostRecentInqexcl7days_8)

if NetFractionRevolvingBurden == -8:
    NetFractionRevolvingBurden_8 = 1
else: NetFractionRevolvingBurden_8 = 0
model_Features = np.append(model_Features, NetFractionRevolvingBurden_8)

if NetFractionInstallBurden == -8:
    NetFractionInstallBurden_8 = 1
else: NetFractionInstallBurden_8 = 0
model_Features = np.append(model_Features, NetFractionInstallBurden_8)

if NumRevolvingTradesWBalance == -8:
    NumRevolvingTradesWBalance_8 = 1
else: NumRevolvingTradesWBalance_8 = 0
model_Features = np.append(model_Features, NumRevolvingTradesWBalance_8)

if NumInstallTradesWBalance == -8:
    NumInstallTradesWBalance_8 = 1
else: NumInstallTradesWBalance_8 = 0
model_Features = np.append(model_Features, NumInstallTradesWBalance_8)

if NumBank2NatlTradesWHighUtilization == -8:
    NumBank2NatlTradesWHighUtilization_8 = 1
else: NumBank2NatlTradesWHighUtilization_8 = 0
model_Features = np.append(model_Features, NumBank2NatlTradesWHighUtilization_8)

if PercentTradesWBalance == -8:
    PercentTradesWBalance_8 = 1
else: PercentTradesWBalance_8 = 0
model_Features = np.append(model_Features, PercentTradesWBalance_8)


# demos
# if (selected_demos == "Demo1"):
#     st.session_state.MSinceMostRecentDelq = 100


# if (selected_demos == "Demo1"):
#     ExternalRiskEstimate = col2.number_input('ExternalRiskEstimate(Decreasing)', -7, 100, 54, 1, key = "ExternalRiskEstimate", on_change = update_ExternalRiskEstimate_slider)
#     MSinceOldestTradeOpen = col2.number_input('MSinceOldestTradeOpen(Decreasing)', -7, 810, 88, 1, key = "MSinceOldestTradeOpen", on_change = update_MSinceOldestTradeOpen_slider)
#     MSinceMostRecentTradeOpen = col2.number_input('MSinceMostRecentTradeOpen(Decreasing)', -7, 400,7,1, key = "MSinceMostRecentTradeOpen", on_change = update_MSinceMostRecentTradeOpen_slider)
#     AverageMInFile = col2.number_input('AverageMInFile(Decreasing)', -7, 400,37,1, key = "AverageMInFile", on_change = update_AverageMInFile_slider)
#     NumSatisfactoryTrades = col2.number_input('NumSatisfactoryTrades(Decreasing)', -7, 80,25,1, key = "NumSatisfactoryTrades", on_change = update_NumSatisfactoryTrades_slider)
#     NumTrades60Ever2DerogPubRec = col2.number_input('NumTrades60Ever2DerogPubRec(Increasing)', -7, 20,0,1, key = "NumTrades60Ever2DerogPubRec", on_change = update_NumTrades60Ever2DerogPubRec_slider)
#     NumTrades90Ever2DerogPubRec = col2.number_input('NumTrades90Ever2DerogPubRec(Increasing)', -7, 20,0,1, key = "NumTrades90Ever2DerogPubRec", on_change = update_NumTrades90Ever2DerogPubRec_slider)
#     PercentTradesNeverDelq = col2.number_input('PercentTradesNeverDelq(Decreasing)', -7, 100,92,1, key = "PercentTradesNeverDelq", on_change = update_PercentTradesNeverDelq_slider)
#     MSinceMostRecentDelq = col2.number_input('MSinceMostRecentDelq(Decreasing)', -7, 90,9,1, key = "MSinceMostRecentDelq", on_change = update_MSinceMostRecentDelq_slider)
#     MaxDelq2PublicRecLast12M = col2.number_input('MaxDelq2PublicRecLast12M(Decreasing)', -7, 7,4,1, key = "MaxDelq2PublicRecLast12M", on_change = update_MaxDelq2PublicRecLast12M_slider)
#     MaxDelqEver = col2.number_input('MaxDelqEver(Decreasing)', -7, 5,6,1, key = "MaxDelqEver", on_change = update_MaxDelqEver_slider)
#     NumTotalTrades = col2.number_input('NumTotalTrades(No constraint)', -7, 110,26,1, key = "NumTotalTrades", on_change = update_NumTotalTrades_slider)
#     NumTradesOpeninLast12M = col2.number_input('NumTradesOpeninLast12M(Increasing)', -7, 20,3,1, key = "NumTradesOpeninLast12M", on_change = update_NumTradesOpeninLast12M_slider)
#     PercentInstallTrades = col2.number_input('PercentInstallTrades(No constraint)', -7, 100,58,1, key = "PercentInstallTrades", on_change = update_PercentInstallTrades_slider)
#     MSinceMostRecentInqexcl7days = col2.number_input('MSinceMostRecentInqexcl7days(Decreasing)', -7, 30,0,1, key = "MSinceMostRecentInqexcl7days", on_change = update_MSinceMostRecentInqexcl7days_slider)
#     NumInqLast6M = col2.number_input('NumInqLast6M(Increasing)', -7, 70,4,1, key = "NumInqLast6M", on_change = update_NumInqLast6M_slider)
#     NumInqLast6Mexcl7days = col2.number_input('NumInqLast6Mexcl7days(Increasing)', -7, 70,4,1, key = "NumInqLast6Mexcl7days", on_change = update_NumInqLast6Mexcl7days_slider)
#     NetFractionRevolvingBurden = col2.number_input('NetFractionRevolvingBurden(Increasing)', -7, 240,89,1, key = "NetFractionRevolvingBurden", on_change = update_NetFractionRevolvingBurden_slider)
#     NetFractionInstallBurden = col2.number_input('NetFractionInstallBurden(Increasing)', -7, 480,76,1, key = "NetFractionInstallBurden", on_change = update_NetFractionInstallBurden_slider)
#     NumRevolvingTradesWBalance = col2.number_input('NumRevolvingTradesWBalance(No constraint)', -7, 40,7,1, key = "NumRevolvingTradesWBalance", on_change = update_NumRevolvingTradesWBalance_slider)
#     NumInstallTradesWBalance = col2.number_input('NumInstallTradesWBalance(No constraint)', -7, 30,7,1, key = "NumInstallTradesWBalance", on_change = update_NumInstallTradesWBalance_slider)
#     NumBank2NatlTradesWHighUtilization = col2.number_input('NumBank2NatlTradesWHighUtilization(Increasing)', -7, 20,2,1, key = "NumBank2NatlTradesWHighUtilization", on_change = update_NumBank2NatlTradesWHighUtilization_slider)
#     PercentTradesWBalance = col2.number_input('PercentTradesWBalance(No constraint)', -7, 100,100,1, key = "PercentTradesWBalance", on_change = update_PercentTradesWBalance_slider)

coefficients = np.array([-3.53678745e-02, -2.27599821e-04,  7.26148977e-03, -9.16206905e-03,
                        -2.97568779e-02,  7.26980325e-02,  1.91643318e-02, -9.05181723e-03,
                        -8.86938343e-03, -5.68631637e-02,  5.04109690e-02, -1.53515900e-03,
                        1.47105960e-02,  7.39073623e-03, -5.28907409e-02,  4.04853892e-01,
                        -3.45854459e-01,  1.16829380e-02,  3.30869176e-03,  9.25539644e-02,
                        -6.30070332e-03,  7.21658764e-02, -2.84812540e-03, -4.63516625e-01,
                        3.65475839e-01,  1.20906456e-01,  3.04508626e-01, -9.84095195e-01,
                        -1.39973528e-02,  3.75452838e-02, -5.96324419e-02,  6.97259779e-02,
                        7.12328632e-01, -1.79626541e+00,  3.98167621e+00])
intercept = 3.98167621

prediction = np.dot(model_Features, coefficients) # + intercept
riskScore = 1/(1+np.exp(-1*prediction))

if run:
    # output
    # col3.header("Output")
    col3.write("This is the Risk Performance estimated from our model")

    delta = "{:.2%} compared with the average.".format((riskScore - 0.5)/0.5)
    if riskScore >= 0.5:
        col3.metric(label = "Risk Decision", value = "High Risk", delta= delta, delta_color = "inverse")
        # col3.subheader("High Risk")
    elif riskScore < 0.5:
        col3.metric(label = "Risk Decision", value = "Low Risk", delta= delta, delta_color = "inverse")
        # col3.subheader("Low Risk")


    text = "There is {:.0%} risk of default for this candidate".format(riskScore)
    col3.subheader(text)

    # risk score plot --dataframe
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from scipy.special import expit



    ### create a defualt plot
    scorePlot = pd.DataFrame(columns = ("Risk Score", "Associated Risk Estimated"))
    riskRange = np.arange(-6, 6, 0.01).tolist()

    for i in range(0, len(riskRange)):
        newrow = [riskRange[i], expit(riskRange[i])]
        scorePlot.loc[i] = newrow

    # risk score plot -- plot
    fig, ax = plt.subplots()

    ax = sns.lineplot(data=scorePlot, x = "Risk Score", y = "Associated Risk Estimated")
    ax.scatter(prediction, riskScore, color = "red")
    ax.hlines(riskScore, xmin = -6, xmax = prediction, color = "red")
    ax.vlines(prediction, ymin = 0, ymax = riskScore, color = "red")
    plt.xlim([-6,6])
    plt.ylim([0,1])
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # add plot
    col3.pyplot(fig)

    # other scores info
    overallScore = prediction - intercept
    outputInfo = pd.DataFrame({"Overall Score": [overallScore], "Bias": [intercept], "Risk Score": [prediction], "Associated Risk": [riskScore]})
    col3.table(outputInfo)

    # feature box plot
    new_df = pd.read_csv("new_df.csv")
    new_df = new_df.iloc[:,1:24]
    col3.subheader("Historical data distribution of all features")

    fig, ax = plt.subplots()

    ax.boxplot(np.array(new_df))
    col3.pyplot(fig)



    # five most similar cases

    st.header("5 Most Similar Cases")
    st.write("Here are five most similar cases based on current features.")

    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.neighbors import NearestNeighbors

    dataset = pd.read_csv("heloc_dataset_v1.csv")
    X_train = dataset.iloc[:,1:25]
    y_train = dataset['RiskPerformance'].map(dict(Bad = 1, Good = 0))
    knn_input = np.array([ExternalRiskEstimate, MSinceOldestTradeOpen, MSinceMostRecentTradeOpen, AverageMInFile, NumSatisfactoryTrades, NumTrades60Ever2DerogPubRec, NumTrades90Ever2DerogPubRec, PercentTradesNeverDelq, MSinceMostRecentDelq,MaxDelq2PublicRecLast12M,MaxDelqEver,NumTotalTrades,NumTradesOpeninLast12M,PercentInstallTrades,MSinceMostRecentInqexcl7days,NumInqLast6M,NumInqLast6Mexcl7days,NetFractionRevolvingBurden,NetFractionInstallBurden,NumRevolvingTradesWBalance,NumInstallTradesWBalance,NumBank2NatlTradesWHighUtilization,PercentTradesWBalance])


    # knn_model = KNeighborsRegressor(n_neighbors=5)
    # knn_model.fit(X_train, y_train)
    # knn = knn_model.predict([knn_input])

    samples = NearestNeighbors(n_neighbors=5)
    samples.fit(X_train, y_train)
    knn_output = samples.kneighbors([knn_input])



    knn_df = dataset.iloc[[knn_output[1].item(0)]]
    knn_df = knn_df.append(dataset.iloc[[knn_output[1].item(1)]])
    knn_df = knn_df.append(dataset.iloc[[knn_output[1].item(2)]])
    knn_df = knn_df.append(dataset.iloc[[knn_output[1].item(3)]])
    knn_df = knn_df.append(dataset.iloc[[knn_output[1].item(4)]])
    # knn_df = knn_df.append(knn_input)
    # knn_df = pd.concat([pd.DataFrame(knn_input), knn_df], ignore_index=True)


    if riskScore < 0.5: 
        Estimated = "Good"
    else: 
        Estimated = "Bad"

    current1 = pd.DataFrame(knn_input.flatten(), columns=["current"])
    current = pd.DataFrame(columns= ["Index"] + knn_df.columns.values.tolist())
    knn_input = ["Current", Estimated] + current1["current"].tolist()
    current.loc[0]= knn_input
    current = current.set_index("Index")

    knn_index = knn_df.index.tolist()
    knn_df = pd.concat([current, knn_df], ignore_index=True)
    for i in range(len(knn_index)):
        knn_index[i] = str(knn_index[i])
    knn_df["Index"] = ["Current"]+knn_index
    knn_df = knn_df.set_index("Index")

    st.dataframe(knn_df)


# appendix
st.header("Appendix")

st.subheader("Feature Explanations")
df = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "Data Dictionary", index_col=None)
pd.options.display.max_colwidth = 100
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.dataframe(df)

st.subheader("MaxDelq Table")
st.caption("MaxDelq2PublicRecLast12M")
df2 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "MaxDelq2PublicRecLast12M", index_col=None)
df2 = df2.astype(str)
st.dataframe(df2)
st.caption("MaxDelqEver")
df3 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "MaxDelqEver", index_col=None)
st.dataframe(df3)

st.subheader("Special Values")
df4 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "SpecialValues", index_col=None)
st.dataframe(df4) #Dictionary, index_col=None)
# pd.options.display.max_colwidth = 100
# hide_table_row_index = """
#             <style>
#             tbody th {display:none}
#             .blank {display:none}
#             </style>
#             """
# st.markdown(hide_table_row_index, unsafe_allow_html=True)
# st.dataframe(df)

# st.subheader("MaxDelq Table")
# st.caption("MaxDelq2PublicRecLast12M")
# df2 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "MaxDelq2PublicRecLast12M", index_col=None)
# df2 = df2.astype(str)
# st.dataframe(df2)
# st.caption("MaxDelqEver")
# df3 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "MaxDelqEver", index_col=None)
# st.dataframe(df3)

# st.subheader("Special Values")
# df4 = pd.read_excel("heloc_data_dictionary.xlsx", sheet_name = "SpecialValues", index_col=None)
# st.dataframe(df4)