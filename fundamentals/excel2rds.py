# import psycopg2
import pandas as pd
import numpy as np

###--------------------------------------------------------------------------------
## RDS connaction details
###--------------------------------------------------------------------------------
rds_hostname = 'localhost'
rds_username = 'archuser'
rds_password = 'da1a-6rch'
rds_database = 'data-archive'
rds_port = 15432

###-----------------------------------------------------------------------------------------------
## We have to read the excel file with their sheets, both of them has a header in the first row
###-----------------------------------------------------------------------------------------------
metafile_loc='C:\\Users\\212584156\\Box\\FDLProjects\\DataArchival\\Aug21-release\\excel_tooling\\fdl_arch_metadata.xlsx'
df_schemas= pd.read_excel(metafile_loc, sheet_name= 'schema', header=0)
df_tables= pd.read_excel(metafile_loc, sheet_name= 'table', header=0)

df_schemas.rename({
    'schema_name (database schema name. Ex., adapter, analytics, gog_oscar etc)': 'sheet_name',
    'source_system_name (only if specific source systems have to be filtered for archival)': 'source_system_name',
    'database_type (GP/MemSQL)': 'database_type',
    'schema_type (Mirror/Model)': 'schema_type',
    'frequency (Daily/Weekly/Onetime)': 'frequency',
    'all_tables_flag (Y/N)': 'all_tables_flag (Y/N)',
    'status(Enabled/Disabled)': 'status',
    'instance (GP/SS)': 'instance'
}, axis=1, inplace=True)

df_tables.rename({'status (Enabled/Disabled)':'status'}, axis=1, inplace=True)


###-------------------------------------------------------------------------------------------------------------------------------
## We have to replace NaN values (empty fileds in the excel), they will be represented as an empty string in the database tables
###-------------------------------------------------------------------------------------------------------------------------------
df_s = df_schemas.replace(np.nan, '', regex=True)
df_t = df_tables.replace(np.nan, '', regex=True)

df_s.display()
df_t.display()