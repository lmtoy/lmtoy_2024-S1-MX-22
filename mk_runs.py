#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-22"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["HATLAS_RED_1529"] = \
 [ 112408, 112409, 112410, 112412, 112413, 112414, 112416, 112417, 112418,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["HATLAS_RED_1529"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["HATLAS_RED_1529"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
