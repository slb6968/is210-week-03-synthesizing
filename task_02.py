#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition


SEEK = 'Spanish'

WORDLENGTH = len(SEEK)

FLEMISH = inquisition.SPANISH[:inquisition.SPANISH.find(SEEK)] + 'Flemish' + \
          inquisition.SPANISH[inquisition.SPANISH.find(SEEK) + WORDLENGTH:]

print FLEMISH
