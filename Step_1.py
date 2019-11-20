#
# import json
#import pandas as pd
#
# import uuid
# import csv
# from datetime import date
#
# import math
# import time
# from datetime import datetime
# import datetime

from prefect import task, unmapped, Flow, Parameter


config = dict()

# dev
config['dev_db'] = 'CPS_DB'
config['dev_schema'] = 'CPS_CDODS_STG'
config['dev_warehouse'] = 'CPS_CDODS_ETL_WH'

config['dev_quote_header_raw_table'] = 'NTB_CCWR_QUOTES_HEADER_DATA_RAW'
config['dev_quote_linelevel_raw_table'] = 'NTB_CCWR_QUOTES_LINE_LEVEL_RAW'
config['dev_ci_quotes_table'] = 'NTB_CI_QUOTES'

config['dev_ntb_linelevel_staging_raw'] = 'dev_ntb_linelevel_staging'
config['dev_ntb_headerlevel_staging_raw'] = 'dev_ntb_headerlevel_Staging'

config['dev_quote_linelevel_parsed_table'] = 'NTB_CCWR_QUOTES_LINE_LEVEL_PARSED'
config['dev_quote_headerlevel_parsed_table'] = 'NTB_CCWR_QUOTES_HEADER_LEVEL_PARSED'
config['dev_logging_table'] = 'NTB_CCWR_QUOTES_LOGGING'
config['dev_ntb_linelevel_parsed_Staging'] = 'dev_ntb_linelevel_parsed_staging'
config['dev_secret'] = 'secret/snowflake/dev/cps_cdods_etl_svc/password'
config['dev_snowflake_token'] = 's.5OfXACjLync3mMS1214oUSRq.VTsyF'
config['dev_snowflake_acct'] = 'ciscodev.us-east-1'



# prod
config['prod_db'] = 'CPS_DB'
config['prod_schema'] = 'CPS_CDODS_STG'
config['prod_warehouse'] = 'CPS_CDODS_ETL_WH'

config['prod_quote_header_raw_table'] = 'NTB_CCWR_QUOTES_HEADER_DATA_RAW'
config['prod_quote_linelevel_raw_table'] = 'NTB_CCWR_QUOTES_LINE_LEVEL_RAW'
config['prod_ci_quotes_table'] = 'NTB_CI_QUOTES'

config['prod_ntb_linelevel_staging_raw'] = 'prod_ntb_linelevel_staging'
config['prod_ntb_headerlevel_staging_raw'] = 'prod_ntb_headerlevel_Staging'

config['prod_quote_linelevel_parsed_table'] = 'NTB_CCWR_QUOTES_LINE_LEVEL_PARSED'
config['prod_quote_headerlevel_parsed_table'] = 'NTB_CCWR_QUOTES_HEADER_LEVEL_PARSED'
config['prod_logging_table'] = 'NTB_CCWR_QUOTES_LOGGING'
config['prod_ntb_linelevel_parsed_Staging'] = 'prod_ntb_linelevel_parsed_staging'
config['prod_secret'] = 'secret/snowflake/stg/cps_cdods_etl_svc/password'
config['prod_snowflake_token'] = 's.8471AWQ26sVmrRa8SrIuE6sF.VTsyF'
config['prod_snowflake_acct'] = 'ciscostage.us-east-1'

def set_config(environment, config):
    print(environment)
    if environment == 'Dev':

        parameter_dict = {
            'db': config.get('dev_db'),
            'schema': config.get('dev_schema'),
            'warehouse': config.get('dev_warehouse'),
            'ci_quotes_table': config.get('dev_ci_quotes_table'),
            'quote_header_raw_table': config.get('dev_quote_header_raw_table'),
            'quote_linelevel_raw_table': config.get('dev_quote_linelevel_raw_table'),
            'linelevel_Staging': config.get('dev_ntb_linelevel_staging_raw'),
            'quote_linelevel_parsed_table': config.get('dev_quote_linelevel_parsed_table'),
            'headerlevel_Staging': config.get('dev_ntb_headerlevel_staging_raw'),
            'quote_headerlevel_parsed_table': config.get('dev_quote_headerlevel_parsed_table'),
            'logging_table': config.get('dev_logging_table'),
            'linelevel_parsed_staging': config.get('dev_ntb_linelevel_parsed_Staging'),
            'secret' : config.get('dev_secret'),
            'snowflake_token': config.get('dev_snowflake_token'),
            'snowflake_acct': config.get('dev_snowflake_acct')

        }

    if environment == 'Prod':

        parameter_dict = {
            'db': config.get('prod_db'),
            'schema': config.get('prod_schema'),
            'warehouse': config.get('prod_warehouse'),
            'ci_quotes_table': config.get('prod_ci_quotes_table'),
            'quote_header_raw_table': config.get('prod_quote_header_raw_table'),
            'quote_linelevel_raw_table': config.get('prod_quote_linelevel_raw_table'),
            'linelevel_Staging': config.get('prod_ntb_linelevel_staging_raw'),
            'quote_linelevel_parsed_table': config.get('prod_quote_linelevel_parsed_table'),
            'headerlevel_Staging': config.get('prod_ntb_headerlevel_staging_raw'),
            'quote_headerlevel_parsed_table': config.get('prod_quote_headerlevel_parsed_table'),
            'logging_table': config.get('prod_logging_table'),
            'linelevel_parsed_staging': config.get('prod_ntb_linelevel_parsed_Staging'),
            'secret': config.get('prod_secret'),
            'snowflake_token': config.get('prod_snowflake_token'),
            'snowflake_acct': config.get('prod_snowflake_acct')

        }

    return parameter_dict


print("hello")


