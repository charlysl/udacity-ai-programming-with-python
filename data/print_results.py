#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# PROGRAMMER: Carlos Sánchez Losada
# DATE CREATED: 2025/01/19                                
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
#

LHW = 18 # left header width
HW = LHW + 5 # header width
HLW = HW + 5 # header line width
CW = 11 # column width

def header(title, value):
        """Print header with given title and value"""
        print("|", format(f"# {title}", f">{LHW}"), f" | {value} |", )
        print("-"*HLW)

def tline(ncols=4):
        """Print table line"""
        n = HW + ncols*(CW+3)
        print("-" * n)

def row(title, cols):
        """Print row with given title and columns"""
        print("|", format(title, f">{HW}"), "|", end="")
        for col in cols:
                print(format(col, f">{CW}"), "|", end="")
        print()

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
        """
        Prints summary results on the classification and then prints incorrectly 
        classified dogs and incorrectly classified dog breeds if user indicates 
        they want those printouts (use non-default values)
        Parameters:
        results_dic - Dictionary with key as image filename and value as a List 
                (index)idx 0 = pet image label (string)
                        idx 1 = classifier label (string)
                        idx 2 = 1/0 (int)  where 1 = match between pet image and 
                                classifer labels and 0 = no match between labels
                        idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                                0 = pet Image 'is-NOT-a' dog. 
                        idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                'as-a' dog and 0 = Classifier classifies image  
                                'as-NOT-a' dog.
        results_stats_dic - Dictionary that contains the results statistics (either
                        a  percentage or a count) where the key is the statistic's 
                        name (starting with 'pct' for percentage or 'n' for count)
                        and the value is the statistic's value 
        model - Indicates which CNN model architecture will be used by the 
                classifier function to classify the pet images,
                values must be either: resnet alexnet vgg (string)
        print_incorrect_dogs - True prints incorrectly classified dog images and 
                                False doesn't print anything(default) (bool)  
        print_incorrect_breed - True prints incorrectly classified dog breeds and 
                                False doesn't print anything(default) (bool) 
        Returns:
                None - simply printing results.
        """    
    
#     print("model:", model)
#     print()
#     print("number of images:\t\t\t\t\t", results_stats_dic["n_images"])
#     print("number of dog images:\t\t\t\t\t", results_stats_dic["n_dogs_img"])
#     print("number of NON-dog images:\t\t\t\t", results_stats_dic["n_notdogs_img"])
#     print("number of matches between pet & classifier labels:\t", results_stats_dic["n_match"])
#     print("number of correctly classified dog images:\t\t", results_stats_dic["n_correct_dogs"])
#     print("number of correctly classified NON-dog images:\t\t", results_stats_dic["n_correct_notdogs"])
#     print("number of correctly classified dog breeds:\t\t", results_stats_dic["n_correct_breed"])
#     print("percentage of correct matches:\t\t\t\t", results_stats_dic["pct_match"])
#     print("percentage of correctly classified dogs:\t\t", results_stats_dic["pct_correct_dogs"])
#     print("percentage of correctly classified dog breeds:\t\t", results_stats_dic["pct_correct_breed"])
#     print("percentage of correctly classified NON-dogs:\t\t", results_stats_dic["pct_correct_notdogs"])
                
#     if print_incorrect_dogs:
#         print()
#         print("incorrect dogs:")
#         for key, val in results_dic.items():
#             if val[3] != val[4]:
#                 print(key)

#     if print_incorrect_breed:
#         print()
#         print("incorrect breed:")
#         for key, val in results_dic.items():
#             if val[3] and not val[2]:
#                 print(key)

        # percentages
        pcts = map(lambda x: f"{x*100}%", [
                results_stats_dic["pct_correct_notdogs"],
                results_stats_dic["pct_correct_dogs"],
                results_stats_dic["pct_correct_breed"],
                results_stats_dic["pct_match"],
                ])

        print()

        # Print header
        print("-"*HLW)
        header("Total Images", results_stats_dic["n_images"])
        header("Dog Images", results_stats_dic["n_dogs_img"])
        header("Not-a-Dog Images", results_stats_dic["n_notdogs_img"])

        print()

        # Print table
        tline()
        row("", ["% Not-a-Dog", "% Dogs", "% Breeds", "% Match"])
        row("CNN Model Architecture", ["Correct"]*3 + ["Labels"])
        tline()
        row(model, pcts)
        tline()