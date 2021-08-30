#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import itertools


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
            if float(row[1]) > 0:
                # Calculate profits
                round_profit = round((float(row[1])*float(row[2]))/100, 2)
                # Create a list of all actions if data is usable
                elements_once.append(
                    [row[0], float(row[1]), round_profit])
    return elements_once


def force_brute(max_money, elements):
    """
    Description: Checking every combination and chose the better one.
    :param max_money: Money.
    :param elements: List from open(data_doc)

    :return final_combination: list of actions chosen 
    :return final_cost: total spent. 
    :return final_profits: total profits.
    """
    length = len(elements)
    i = 1
    remaining_combinations = []
    # Search every combination of 1:n elements
    while i <= length:
        combination = list(itertools.combinations(elements, i))
        i += 1
        for possibilities in combination:
            cost = 0
            profit = 0
            for element in possibilities:
                # Add costs
                cost += float(element[1])
                # Add profits
                profit += float(element[2])
            # Checking if cost > max_money and append possibilities
            if cost <= float(max_money):
                remaining_combinations.append({'combination': possibilities,
                                               'cost': cost, 'profit': profit})
    # Sort for have list[0] better  solution.
    sorted_combinations = sorted(
        remaining_combinations, key=lambda k: k['profit'], reverse=True)

    # Organise results for show
    final_combination = f'COMBINATION : {[x[0] for x in sorted_combinations[0]["combination"]]}'
    final_cost = f'COST : {(sorted_combinations[0]["cost"])}'
    final_profits = f'PROFITS : {(sorted_combinations[0]["profit"])}'
    return final_combination, final_cost, final_profits


# call and show
print(force_brute(500, open_data('data_brute_force.csv')))
