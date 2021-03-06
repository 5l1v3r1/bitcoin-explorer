#!/usr/bin/env python

from canari.framework import configure
from common.entities import BitcoinTransaction, TransactionDate
from canari.maltego.message import MaltegoException

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2014, Bitcoin-explorer Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@igetshells.io'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='To Transaction Date [Bitcoin-Explorer]',
    description='Returns transaction date of a bitcoin transaction',
    uuids=[ 'bitcoin-explorer.v2.BitcoinTransactionToTransactionDate' ],
    inputs=[ ( 'Bitcoin Explorer', BitcoinTransaction) ],
    remote=False,
    debug=False
)

def dotransform(request, response, config):

    try:
        e = TransactionDate(request.fields['date'])
        response += e

        return response

    except Exception as e:
        raise MaltegoException('An error occured: %s' % e)
