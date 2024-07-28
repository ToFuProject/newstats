
import os

import pprint
import requests
import datastock as ds
# import newspaper



# #########################################################
# #########################################################
#              MAIN
# #########################################################


def main(
    # inputs
    keywords=None,
    # resources
    url=None,
    secret=None,
    # output
    verb=None,
    returnas=None,
):

    # ------------
    # check inputs
    # ------------

    url, secret, verb = _check(
        url=url,
        secret=secret,
        verb=verb,
    )

    # ---------------
    # set parameters
    # ---------------

    # Specify the query and
    # number of returns
    parameters = {
        'q': keywords, # query phrase
        'pageSize': 100,  # maximum is 100
        'apiKey': secret # your own API key
    }

    # -----------------
    # Make the request
    # -----------------

    response = requests.get(
        url,
        params=parameters,
    )

    # ----------
    # extract output
    # ----------

    # Convert the response to JSON
    response_json = response.json()

    # ----------
    # verbosity
    # ----------

    if verb is True:
        # pretty print it
        pprint.pprint(response_json)

    # -----------------
    # Return format
    # -----------------

    out = _return(
        response_json,
        returnas=returnas,
    )

    return out


# #########################################################
# #########################################################
#              _check
# #########################################################


def _check(
    url=None,
    secret=None,
    # output
    verb=None,
    returnas=None,
):

    # ----------
    # url
    # ----------

    url = ds._generic_check._check_var(
        url, 'url',
        default='https://newsapi.org/v2/everything?',
        types=str,
    )

    # ----------
    # secret
    # ----------

    secret = ds._generic_check._check_var(
        secret, 'secret',
        default='67dfd863585444ddb8d961f5988c141b',
        types=str,
    )

    # ----------
    # verb
    # ----------

    verb = ds._generic_check._check_var(
        verb, 'verb',
        default=True,
        types=bool,
    )

    # ----------
    # returnas
    # ----------

    returnas = ds._generic_check._check_var(
        returnas, 'returnas',
        default='Collection',
        allowed=['Collection', 'json', dict, False],
    )

    return url, secret, verb, returnas


# #########################################################
# #########################################################
#              returnas
# #########################################################


def _return(
    response_json=None,
    returnas=None,
):

    # ----------------
    # json
    # ---------------

    if returnas == 'json':

        out = response_json

    # ----------------
    # json
    # ---------------

    elif returnas is dict:

        out = dict(response_json)

    # ----------------
    # False
    # ---------------

    elif returnas is False:

        out = None

    # ----------------
    # Collection
    # ---------------

    elif returnas == 'Collection' or issubclass(returnas, ds.Collection):

        # initialize
        if returnas == 'Collection':
            out = ds.Collection()
        else:
            out = returnas

    return out
