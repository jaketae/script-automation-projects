# radio-log-converter

As a radio telecommunications operator at the USAG Yongsan, I was assigned the task of creating log files of radio calls ("RTO log"), as well as a corresponding incident tracker. While writing the RTO log required manual work, I realized that the process of generating an incident tracker from an RTO log could be automated.

This script receives a `.pdf` RTO log file as input and outputs an incident tracker in `.xlsx` file format. It utilizes the `tabula-py` module to convert a `.pdf` file into a `pandas` dataframe, after which wrangling is performed to clean the data into desired format. Then, a series of row and column operations are performed to mold the dataframe according to the conventions of writing an incident tracker. Exporting this dataframe as `.xlsv` is the last step of the process. 

Although the versatility or portability of this script is somewhat limited by the fact that it deals with very specific files, feel free alter parts of the code for use in other contexts.
