#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-22"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["HATLAS_RED_1529"] = [ 112408, 112409, 112410, 112412, 112413, 112414, 112416, 112417, 112418,
                          112656, 112657, 112658, 112660, 112661, 112662, 112666, 112667, 112668,
                          112670, 112671, 112672, 113212, 113213, 113214, 113216, 113217, 113218,
                          113220, 113221, 113222, 113581, 113582, 113583, 113654, 113794, 113795,]

on["HATLAS_RED_1801"] =  [-113657, 113658, 113659, 113798, 113799, 113800,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["HATLAS_RED_1529"] = ""
pars1["HATLAS_RED_1801"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["HATLAS_RED_1529"] = ""
pars2["HATLAS_RED_1801"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
