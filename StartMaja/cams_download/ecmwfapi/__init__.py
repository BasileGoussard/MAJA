#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# (C) Copyright 2012-2013 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from ecmwfapi import api


__all__ = [
    "ECMWFDataServer",
    "ECMWFService",
]


__version__ = api.VERSION

ECMWFDataServer = api.ECMWFDataServer

ECMWFService = api.ECMWFService
