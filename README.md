# Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Overview](README.md#overview)
1. [Run the Code](README.md#run-the-code)
1. [Output](README.md#output)
1. [Testsuits](README.md#testsuits)
1. [Contacts](README.md#contacts)

# Problem

Given solution is implemented in Python3 for coding challenge of Insight Data Engineer Fellowship. Solution generates a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which is listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Overview

Main purpose of this coding challenge to assess coding skills and understanding of computer science fundamentals as they are both prerequisites of becoming a data engineer. As we are only allowed to use the default data structures that come with that programming language (you might use I/O libraries). For example, you can code in Python, but you should not use Pandas or any other external libraries. 

1. Error handling : File I/O and type casting errors, validation of input data.
2. For a faster insertion and search, the Hash Table is implemented using built-in data type dictionary in python.
3. Implemented using argparse, os, csv and decimal built-in python(3) libraries.

# Run the Code

To run the code, go to pharmacy_counting folder and run "./run.sh" : pharmacy_counting~$./run.sh
(You may need to change the permission for run.sh script by using "chmod +x run.sh" command.)

The Output can be found @pharmacy_counting/output/top_cost_drug.txt. 


# Output 

Output file is comma (`,`) separated fields in each line.

Each line of this file contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

For example

If your input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

then your output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

These files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.

# Testsuits

Testsuits are implemented as per quality code, along with given sample test case.

 * test_1: tests file given by INSIGHT
 * test_2: tests whether code can deal with DRUG_COST=0 (Also, Floating point precision to assure same result)
 * test_3: tests whether code can deal with Invalid DRUG_COST= -400
 * test_4: tests whether code can deal with Invalid PRES_ID = -1000000003
 * test_5: tests whether code can work with 150 records with UNIQUE PRES_ID's.
 * test_6: tests the result when extra name with UNIQUE PRES_ID but DRUG_NAME Has "-"
 * test_7: tests whether code can deal with MISSING Values in Data Item

## Repo directory structure


    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy_counting.py
    |   └── helper_functions.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
	    . . .
	    . . .
	    . . .
	    . . .
            ├── test_7
                ├── input
                │   └── itcont.txt
                |── output
                    └── top_cost_drug.txt


# Contacts
Questions? Please feel free to connect over email (sdesai8@binghamton.edu)
Thank you,
Savankumar Desai
