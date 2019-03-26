# Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Overview](README.md#overview)
1. [Run the Code](README.md#run-the-code)
1. [Output](README.md#output)

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


## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
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
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt

**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `pharmacy-counting.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing your directory structure and output format

To make sure that your code has the correct directory structure and the format of the output files are correct, we have included a test script called `run_tests.sh` in the `insight_testsuite` folder.

The tests are stored simply as text files under the `insight_testsuite/tests` folder. Each test should have a separate folder with an `input` folder for `itcont.txt` and an `output` folder for `top_cost_drug.txt`.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 

On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed



One test has been provided as a way to check your formatting and simulate how we will be running tests when you submit your solution. We urge you to write your own additional tests. `test_1` is only intended to alert you if the directory structure or the output for this test is incorrect.

Your submission must pass at least the provided test in order to pass the coding challenge.

For a limited time we also are making available a <a href="http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link">website</a> that will allow you to simulate the environment in which we will test your code. It has been primarily tested on Python code but could be used for Java and C++ repos. Keep in mind that if you need to compile your code (e.g., javac, make), that compilation needs to happen in the `run.sh` file of your code repository. For Python programmers, you are able to use Python2 or Python3 but if you use the later, specify `python3` in your `run.sh` script.

# Questions?
Email us at cc@insightdataengineering.com
