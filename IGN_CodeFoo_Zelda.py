#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Stephen Montague
Date: 15 March 2020
Title: IGN Code Foo submission.  Quests for Link.
https://www.ign.com/code-foo/2020

Summary:

Link of Zelda needs to collect the max Rupees possible 
by selecting the best mix of quests from a Quest Board,
and without allowing quest dates to overlap. 

This is done here by AI that models the Quest Board as a Constraint Satisfaction Problem (CSP).

Directions:

Depends on import of module "python-constraint" (in PyCharm, maybe the 2nd auto-import offered) or run:

        pip install python-constraint

Module info: https://pypi.org/project/python-constraint/

"""

from constraint import *

# INSTANTIATE CSP

problem = Problem()

# ADD VARIABLES (QUESTS) & DOMAINS (POSSIBLE REWARDS)

problem.addVariable('quest1', [0, 750])
problem.addVariable('quest2', [0, 500])
problem.addVariable('quest3', [0, 920])
problem.addVariable('quest4', [0, 1050])
problem.addVariable('quest5', [0, 200])
problem.addVariable('quest6', [0, 400])
problem.addVariable('quest7', [0, 1200])
problem.addVariable('quest8', [0, 370])
problem.addVariable('quest9', [0, 840])
problem.addVariable('quest10', [0, 165])
problem.addVariable('quest11', [0, 1520])
problem.addVariable('quest12', [0, 600])
problem.addVariable('quest13', [0, 430])
problem.addVariable('quest14', [0, 1100])
problem.addVariable('quest15', [0, 590])
problem.addVariable('quest16', [0, 900])
problem.addVariable('quest17', [0, 230])
problem.addVariable('quest18', [0, 1120])
problem.addVariable('quest19', [0, 460])
problem.addVariable('quest20', [0, 780])
problem.addVariable('quest21', [0, 410])
problem.addVariable('quest22', [0, 570])
problem.addVariable('quest23', [0, 1200])
problem.addVariable('quest24', [0, 2100])

# ADD CONSTRAINTS

questDates = {
    "quest1": {1, 2, 3},
    "quest2": {2, 3},
    "quest3": {1, 2, 3, 4},
    "quest4": {3, 4, 5, 6, 7, 8, 9, 10},
    "quest5": {5},
    "quest6": {3, 4, 5, 6},
    "quest7": {7, 8, 9, 10, 11},
    "quest8": {12, 13, 14},
    "quest9": {6, 7, 8, 9, 10, 11, 12, 13},
    "quest10": {19, 20},
    "quest11": {23, 24, 25, 26, 27, 28, 29},
    "quest12": {14, 15, 16, 17},
    "quest13": {8, 9, 10},
    "quest14": {20, 21, 22, 23, 24, 25, 26},
    "quest15": {28, 29, 30},
    "quest16": {10, 11, 12, 13},
    "quest17": {13, 14, 15, 16, 17, 18},
    "quest18": {25, 26, 27, 28},
    "quest19": {9},
    "quest20": {16, 17, 18, 19, 20, 21, 22, 23, 24, 25},
    "quest21": {4, 5, 6, 7, 8},
    "quest22": {11, 12, 13},
    "quest23": {7, 8},
    "quest24": {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
}


def hasEitherOrNeither(questA, questB):
    # Returns True only if one or both parameters equal zero.
    return questA == 0 or questB == 0


# Check each quest-set for intersection with all other quest-sets.
# For each intersection, add constraint.

UPPER_BOUND = len(questDates)
NEXT_UPPER_BOUND = UPPER_BOUND + 1
for questNum in range(1, UPPER_BOUND):
    for nextQuestNum in range(questNum + 1, NEXT_UPPER_BOUND):
        if questDates["quest" + str(questNum)] & questDates["quest" + str(nextQuestNum)]:
            problem.addConstraint(hasEitherOrNeither, ["quest" + str(questNum), "quest" + str(nextQuestNum)])

# SOLVE CSP

solutions = problem.getSolutions()

maxReward = 0
maxIndex = 0
for index, element in enumerate(solutions):
    sumReward = sum(element.values())
    if sumReward > maxReward:
        maxReward = sumReward
        maxIndex = index

solution = solutions[maxIndex]

# CLEAN DATA: Remove quests not taken

for quest in list(solution):
    if solution[quest] == 0:
        del solution[quest]

# ASSIGN START DATES

startDates = {
    "quest1": 1,
    "quest2": 2,
    "quest3": 1,
    "quest4": 3,
    "quest5": 5,
    "quest6": 3,
    "quest7": 7,
    "quest8": 12,
    "quest9": 6,
    "quest10": 19,
    "quest11": 23,
    "quest12": 14,
    "quest13": 8,
    "quest14": 20,
    "quest15": 28,
    "quest16": 10,
    "quest17": 13,
    "quest18": 25,
    "quest19": 9,
    "quest20": 16,
    "quest21": 4,
    "quest22": 11,
    "quest23": 7,
    "quest24": 2
}

for quest in list(startDates):
    if quest not in solution:
        del startDates[quest]

questOrder = startDates

# PREP PRINTING: Replace quest ID with quest name

questNames = {
    "quest1": "Robbie's Research",
    "quest2": "A Parent's Love",
    "quest3": "The Weapon Connoisseur",
    "quest4": "Sunshroom Sensing",
    "quest5": "Sunken Treasure",
    "quest6": "Cooking with Koko",
    "quest7": "Arrows of Burning Heat",
    "quest8": "Stalhorse: Pictured!",
    "quest9": "Curry for What Ails You",
    "quest10": "The Jewel Trade",
    "quest11": "Slated for Upgrades",
    "quest12": "Medicinal Molduga",
    "quest13": "Tools of the Trade",
    "quest14": "A Gift for the Great Fairy",
    "quest15": "A Rare Find",
    "quest16": "Frog Catching",
    "quest17": "Luminous Stone Gathering",
    "quest18": "A Freezing Rod",
    "quest19": "Rushroom Rush!",
    "quest20": "The Hero's Cache",
    "quest21": "A Gift of Nightshade",
    "quest22": "Lynel Safari",
    "quest23": "Riddles of Hyrule",
    "quest24": "An Ice Guy"
}

for questName in questNames:
    if questName in questOrder:
        questOrder[questNames[questName]] = questOrder.pop(questName)

# SORT BY START DATE

questOrder = {k: questOrder[k] for k in sorted(questOrder, key=questOrder.get)}

# PRINT SOLUTION

print("\nMax Reward:", maxReward, "Rupees")
print("Quest order: ")
for quest, date in questOrder.items():
    print(f"\tDay {date:2}: {quest}")
