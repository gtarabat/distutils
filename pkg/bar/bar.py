#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : bar.py
# Author            : George Arampatzis <garampat@ethz.ch>
# Date              : 31.01.2022 15:00
# Last Modified Date: 31.01.2022 15:33
# Last Modified By  : George Arampatzis <garampat@ethz.ch>

from pkg import foo

def my_print(msg):
    print('----- Inside module bar ------')
    foo.my_print(msg)
    print('------------------------------')
