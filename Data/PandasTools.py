"""
Created by adam on 1/6/20
"""
__author__ = 'adam'



def clean_string_columns( frame ):
    """Removes excess whitespace from column names.
    (I always have to look this up otherwise)
    """
    return frame.columns.str.strip()


if __name__ == '__main__':
    pass