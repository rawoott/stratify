#!/usr/bin/env python3


import sys
import math

num_pcs_cut_off = 3

def inputData(fname):
    pop   = {}
    evecs = []
    pids  = []
    f = open(fname)
    index = 0
    for line in f:
        if line[0]=="#":
            continue
        data = line.strip().split()
        this_pop = data[-1]
        this_id  = data[0]
        pids.append(this_id)
        evecs.append(list(map(float,data[1:-1])))
        if this_pop in pop:
            pop[this_pop].append(index)
        else:
            pop[this_pop]=[index]
        index=index+1
    return evecs, pop, pids
        
def dummy(x):
    # only here to for coverage testing
    x=x+1

def getCentroid(evecs, pc, pop_indivs):
    centre = 0
    for i in pop_indivs: centre = centre+evecs[i][pc]
    return float(centre)/len(pop_indivs)

def getSampleStdDev(evecs, pc, pop_indivs,ave):
    sum_sq = 0
    for i in pop_indivs: 
        sum_sq = sum_sq + (evecs[i][pc]-ave)**2
    return math.sqrt(sum_sq/(len(pop_indivs)-1))


def remOutliers(evecs,pids,pop_indivs):
    excludes = []
    if len(pop_indivs)==0: 
        print("This is an error")
    elif len(pop_indivs)==1:
        return excludes
    for pc in range(num_pcs_cut_off):
        centre = getCentroid(evecs, pc, pop_indivs)
        stdev  = getSampleStdDev(evecs, pc, pop_indivs, centre)
        for i in pop_indivs:
            if abs(evecs[i][pc]-centre)>3*stdev:
                excludes.append(i)
    return excludes

if __name__ == "__main__":
    fname  = sys.argv[1]
    evecs, pop, pids = inputData(sys.argv[1])
    for p in pop:
        excludes = remOutliers(evecs,pids,pop[p])
        print("Exclude in pop %s :"%p,*excludes)
