

import os

import pprint
import datastock as ds
# import newspaper

# loccal
from . import _newsapi


__all__ = ['main']


# #########################################################
# #########################################################
#              MAIN
# #########################################################


def main(
    keywords=None,
    api=None,
):

    # ------------
    # check inputs
    # ------------

    api = _check(
        api=api,
    )

    # -----------------
    # call api
    # -----------------

    if api == 'newsapi':

        dout = _newsapi.main(
            keywords=keywords,
        )

    else:
        raise NotImplementedError()


    return dout


# #########################################################
# #########################################################
#              _check
# #########################################################


def _check(
    api=None,
):

    # ----------
    # api
    # ----------

    api = ds._generic_check._check_var(
        api, 'api',
        default='newsapi',
        types=str,
        allowed=['newsapi'],
    )

    return api


# #########################################################
# #########################################################
#              __MAIN__
# #########################################################


if __name__ == '__main__':
    dout = main()
