"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys
import collections

import nsfg
import thinkstats2


def LoadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    return dct.ReadFixedWidth(dat_file, compression='gzip')


def DictCaseidIdx(df):
    d = collections.defaultdict(list)
    for idx, cid in df.caseid.iteritems():
        d[cid].append(idx)
    return d


def ValidatePregn(resp):
    # read preg data
    preg = nsfg.ReadFemPreg()
    # map from caseid to indices
    preg_map = DictCaseidIdx(preg)
    # loop through respondent pregnum series
    for idx, num_pregn in resp.pregnum.items():
        cid = resp.caseid[idx]  # resp.loc[idx].caseid
        indices = preg_map[cid]
        # check num_pregn from respondent is equal
        # to number of records in pregnancy file
        if len(indices) != num_pregn:
            print(cid, len(indices), num_pregn)
            return False
    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = LoadFemResp()
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[3] == 1110)
    assert(ValidatePregn(resp))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)


# def CleanFemPreg(df):
#    df.agepreg /= 100.0
#    na_vals = [97, 98, 99]
#    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
#    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
#    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
