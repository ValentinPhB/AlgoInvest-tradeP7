#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def open_data(data_doc):
    """
    Description: Open CSV and organise data.
    :param data_doc: .csv.

    :return elements_once: list of data checked [action_name, price, profits].
    """
    with open(data_doc) as csv_file:
        data = list(csv.reader(csv_file))
        elements_once = []
        for row in data[1:]:
            # Checking if price > 0
            if int(float(row[1]) * 100) > 0:
                # Calculate profits
                round_profit = round((float(row[1]) * float(row[2])), 0)
                # Create a list of all actions if data is usable
                elements_once.append(
                    [row[0], int(float(row[1]) * 100), int(round_profit)])
    return elements_once


def optimized_dynamic(max_money, elements):
    """
    Description: Dynamic programming finding better invest.
    :param max_money: Money.
    :param elements: List from open(data_doc)

    :return final_combination: list of actions chosen 
    :return final_cost: total spent. 
    :return final_profits: total profits.
    """
    # Multiplication Needed for floats
    max_bet = max_money * 100
    # Create a table (max_bet  x-axis, element y-axis)
    table = [[0 for x in range(max_bet + 1)]
             for y in range(len(elements) + 1)]

    # Fill table with operations
    for i in range(1, len(elements) + 1):
        for w in range(1, max_bet + 1):
            # Price <= max_bet ? Opportunity. Price added to precedent calculation.
            if elements[i - 1][1] <= w:
                table[i][w] = max(
                    elements[i - 1][2] + table[i - 1][w - elements[i - 1][1]], table[i - 1][w])
            # Element discarded, we take the previous calculation.
            else:
                table[i][w] = table[i - 1][w]

    w = max_bet
    n = len(elements)
    elements_selection = []

    # Browse table and find the better profits, then add all actions to element_selection
    while w >= 0 and n >= 0:
        e = elements[n - 1]
        if table[n][w] == table[n - 1][w - e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    # Organise results for show
    final_combination = f'COMBINATIONS : {[x[0] for x in elements_selection][::-1]}'
    final_cost = f'COST : {(max_bet - w) / 100}'
    final_profits = f'PROFITS : {(table[-1][-1]) / 100}'
    return final_combination, final_cost, final_profits


# call and show
print(optimized_dynamic(500, open_data('dataset2_Python+P7.csv')))
