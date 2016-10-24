# This is not proper CSV parser - it does not handle escape sequences and quotations, also only comma and tab
# are proper separators
import re

split_re = re.compile("[,\t]")

# handling of proper file closing is up to enclosing code
def reader(fh):
    for line in fh:
        yield [str(x).strip() for x in split_re.split(line)]
