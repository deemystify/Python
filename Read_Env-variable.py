#Reading an environmental variable

import  os
os_version = os.getenv('OS')
print(os_version)

# Using dotenv
# Store environmental variables in text file
# Do not hard code, don't check sensitiv values into source control.
#.env file

DATABASE = Sample_Connection_String

# app.py
from dotenv import load_dotenv
import os
load_dotenv()
database = os.getenv('DATABASE')
print(database)