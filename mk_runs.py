#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-22"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["HATLAS_RED_1476"] =  [ 117835, 117836, 117837, 117839, 117840, 117841, 117843, 117844, 117845,
                           118100, 118101, 118102, 118104, 118105, 118106, 118109, 118110, 118111,]

on["HATLAS_RED_1529"] = [ 112408, 112409, 112410, 112412, 112413, 112414, 112416, -112417, 112418,
                          112656, 112657, 112658, 112660, 112661, 112662, 112666, 112667, 112668,
                          112670, 112671, 112672, 113212, 113213, 113214, 113216, 113217, 113218,
                          -113220, 113221, 113222, 113581, 113582, 113583, -113654, -113794, 113795,]

on["HATLAS_RED_1801"] =  [-113657, -113658, -113659, 113798, 113799, 113800,
                           113900, 113901, 113902, 113904, 113905, 113906, 113908, 113909, 113910,
                           113913, 113914, 113915, 113917, 113918, 113919, 113921, 113922, 113923,
                           114039, 114040, 114041, 114043, 114044, 114045, 114047, 114048, 114049,
                           114052, 114053, 114054,
                           117221, 117222, 117223, 117225, 117226, 117227, 117240, 117241, 117242,]

on["HATLAS_RED_2389"] =  [ 117868, 117869, 117870, 117872, 117873, 117874, 117876, 117877, 117878,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["HATLAS_RED_1476"] = ""
pars1["HATLAS_RED_1529"] = "speczoom=91,3"
pars1["HATLAS_RED_1801"] = ""
pars1["HATLAS_RED_2389"] = ""


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["HATLAS_RED_1476"] = ""
pars2["HATLAS_RED_1529"] = ""
pars2["HATLAS_RED_1801"] = ""
pars2["HATLAS_RED_2389"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
