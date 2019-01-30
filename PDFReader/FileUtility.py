"""
    easygui : http://easygui.sourceforge.net/api.html
"""

import os
import easygui
from easygui import *


def getfile(title, defaultpath, msg='Please select a file', filetype="*.*"):
    stmp = ''
    # msg = "Please select the HL7 file to search"

    # filetypes = ["*.hl7", ["*.HL7", "HL7 files"]]
    # filename = easygui.fileopenbox(msg=msg, title=title, filetypes=filetypes, multiple=False)
    filename = easygui.fileopenbox(msg=msg, title=title, default=filetype,
                                   multiple=False)
    if filename:
        print("Selected file: " + filename)
        name, ext = os.path.splitext(filename)
        #        if ".hl7" != str(ext).lower():
        #            stmp = f"Invalid file name: {filename}"
        #            return (None, stmp)

        # test if file exists
        if not os.path.isfile(filename):
            stmp = "File not found"
            return (None, stmp)
        else:
            return (filename, '')
    else:
        return (None, 'Cancel')


def hl7search(title):
    errmsg = ''
    fieldNames = ["Segment", "field", "data"]
    fieldValues = []
    while True:
        if len(errmsg) > 0:
            msg = errmsg
        else:
            msg = "Enter search parameters {HL7 Segment, Field, value:[can be blank]}"

        fieldValues = multenterbox(msg, title, fieldNames)
        if fieldValues == None:
            return (fieldValues, 'Cancel')

        errmsg = ''
        for i in range(len(fieldNames) - 1):  # don't make data required
            if fieldValues[i].strip() == "":
                errmsg = errmsg + f'Entry {fieldNames[i]} is required\n\n'
        if errmsg == "":
            break

    return (fieldValues, '')
