import json
from math import sqrt

def load_journal(fname):
    f = open (fname, "r")
    data = json.load(f)
    
    return data
    
def compute_phi(fname, event):
    
    data = load_journal(fname)
    
    n11=0
    n10=0
    n01=0
    n00=0
    
    for i in data:
        if event in i["events"] and i["squirrel"] == True:
            n11 += 1
        if event in i["events"] and i["squirrel"] == False:
            n10 += 1
        if event not in i["events"] and i["squirrel"] == True:
            n01 += 1
        if event not in i["events"] and i["squirrel"] == False:
            n00 += 1
            
    n1_ = n11 + n10
    n0_ = n01 + n00
    n_1 = n01 + n11
    n_0 = n00 + n10
    
    corr=(n11*n00 - n01*n10)/sqrt(n1_ * n0_ * n_1 * n_0)
    return corr
    
def compute_correlations(fname):
    
    data = load_journal(fname)
    corr_dict = dict() 
    
    for i in data:
        for event in i["events"]:
            if event not in corr_dict:
                corr_dict[event] = compute_phi(fname, event)
                
    return corr_dict
    
def diagnose(fname):
    corr_dict = compute_correlations(fname)
    
    corr_dict = sorted(corr_dict, key = lambda item: corr_dict[item])
    return (corr_dict[-1], corr_dict[0])
    
    
    

    
       
