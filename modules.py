#  A module is basically a file containing a set of functions to include in your apllication. There are core python modules, modules you can install using the pip package manager (including django) as well as custom modules

# Core modules
import datetime
# from datetime import date

# pip module
from camelcase import CamelCase



today = datetime.date.today()
# today = date.today()  - importing only date from datetime
c = CamelCase
print(c.hump('hello there world'))

print(today)
