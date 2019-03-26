# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 23:05:00 2019

@author: savan
"""

import os
import csv
import argparse
import helper_functions

def main():
    parser = argparse.ArgumentParser(description = 'Pharmacy Counting Solution')    
    parser.add_argument("inputFile", metavar="in", help="Input file : Prescribers and drug Information")
    parser.add_argument("outputFile", metavar="out", help="Output file : Drug Information with #of unique prescribers and total cost")
    args = parser.parse_args()
    
    try:
        with open(args.inputFile, "r") as inputf:
            in_reader = csv.reader(inputf, delimiter=",")
            next(in_reader)     #Gives next row of the in_reader's iterable object as a list
            drugs = {}      #Dictionary to store drug details
            for i, data in enumerate(in_reader):
                helper_functions.insertDataItem(data, drugs)
    except IOError:
        print("Error in file handling/reading")
        
    paired_drugs = zip(drugs.keys(), drugs.values())
    paired_drugs = list(paired_drugs)
    paired_drugs = sorted(paired_drugs, key=lambda dr: (-dr[1]['drug_cost'], dr[0]))
               
    with open(args.outputFile, "w") as outputf:
        header = ["drug_name", "num_prescriber", "total_cost"]
        out_writer = csv.DictWriter(outputf, fieldnames = header)
        out_writer.writeheader()
        
        for drug_item in paired_drugs:
            out_writer.writerow({"drug_name":drug_item[0], 
                                 "num_prescriber":(len(drug_item[1])-1),
                                 "total_cost":drug_item[1]["drug_cost"]})
        outputf.truncate(outputf.tell() - len(os.linesep))      
        
if __name__ == '__main__':
    main()
