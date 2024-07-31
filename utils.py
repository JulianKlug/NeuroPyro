
def format_date_column(date_column):
    # replace Dez with Dec
    date_column = date_column.str.replace('Dez', 'Dec')
    # replace Okt with Oct
    date_column = date_column.str.replace('Okt', 'Oct')
    # replace Mrz with Mar
    date_column = date_column.str.replace('Mrz', 'Mar')
    # replace Mai with May
    date_column = date_column.str.replace('Mai', 'May')
    # replace Juni with Jun
    date_column = date_column.str.replace('Juni', 'Jun')
    # replace Sept with Sep
    date_column = date_column.str.replace('Sept', 'Sep')
    return date_column