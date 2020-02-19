#!/usr/bin/python3
#
# Ansible Filter to Parse String Data from pyats_diff()
# Written by Nick Thompson (@nsthompson)
# Copyright (C) 2020 World Wide Technology
# All Rights Reserved
#

class FilterModule(object):
    def filters(self):
        return {
            'parse_diff': self.parse_diff
        }

    def parse_diff(self, _variable):
        # Strip Any Whitespace from the String
        _variable = _variable.replace(' ', '')
        # Add ':' between our leading designator (+ or -)
        _variable = _variable.replace('+', '+:')
        _variable = _variable.replace('-', '-:')
        # Build a list
        _variable = _variable.split('\n')

        # Define the structure of our new dictionary
        _dict = { 'added': {}, 'removed': {} }

        # Iterate through the list and build our data structure
        for _i in _variable:
            # Split the list entries at the ':'
            _splitlist = _i.split(':')
            # Add data to _dict based on our leading designator
            if _splitlist[0] == "+":
                _dict['added'].update({ _splitlist[1]: _splitlist[2] })
            elif _splitlist[0] == "-":
                _dict['removed'].update({ _splitlist[1]: _splitlist[2] })

        # Let's get out of here
        return _dict