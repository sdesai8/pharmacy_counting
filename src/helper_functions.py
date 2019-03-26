# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:17:08 2019

@author: savan
"""

from decimal import Decimal

def isPositiveDecimal(number):
    """ 
    To validate if value is positive decimal number  
  
    Parameters: 
    arg1 (string): like example: prescriber_id/drug_cost
        
    Returns: 
    Decimal: Return Updated decimal value otherwise False 

    """
    try:
        tmp = float(number)
        #print("number : " + str(number))
        if tmp >= 0:
            return Decimal(number)
    except ValueError:
        return False
    except TypeError:
        return False
    return False


def isValidationTrue(data):
    """ 
    To validate the data  
  
    Parameters: 
    arg1 (list): [prescriber_id, prescriber_first_name, prescriber_last_name, drug_name, drug_cost]
        
    Returns: 
    list: Return Updated fields with True otherwise False 
  
    """
    
    #length of data item must be 5 as mention in description
    if (len(data) != 5):
        return False
    if (data is None):
        return False
    
    pres_id = isPositiveDecimal(data[0])
    drug_cost = isPositiveDecimal(data[-1])
    #print("pres_id: " + str(pres_id) + "and drug_cost: " +str(drug_cost))
    if (pres_id is not False and drug_cost is not False):
        data[0] = pres_id
        data[-1] = drug_cost
        try:
            data[3] = data[3].replace('-', ' ')
        except AttributeError:
            return False
    else:
        return False
    return data
        
        
def insertDataItem(data, drugs):
    """ 
    Insert data item in drugs dictionary where drug_name is key with dictionary of
    Unique prescriber_id's and total cost as a value.
  
    Parameters: 
    arg1 (list): [prescriber_id, prescriber_first_name, prescriber_last_name, drug_name, drug_cost]
    arg2 (dict): Dictionary of data items
        
    Returns: 
    dict: Dictionary with inserted/updated data items.
  
    """
    if isValidationTrue(data):
        #print("Data item is valid!")
        dic_to_be_inserted = {}
        
        if (data[3] in drugs):
            dic_to_be_inserted = drugs[data[3]]
            if (data[0] not in dic_to_be_inserted):
                dic_to_be_inserted[data[0]] = True
            dic_to_be_inserted['drug_cost'] += data[-1]
        else:
            drugs[data[3]] = dic_to_be_inserted
            dic_to_be_inserted[data[0]] = True
            dic_to_be_inserted['drug_cost'] = data[-1]
    else:
        print("Data item " + str(data) +" is not valid to be insrted in to drugs dictionary")
        return False
    return True
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
