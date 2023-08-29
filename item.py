import pygame, os
from constants import *

class Item():
    def __init__(self, type):
        self.type = type
        self.item_list = {}
        self.item_index = 0

        if type == TOOLS:
            self.add_item(TOOLS)
        elif type == SEEDS:
            self.add_item(SEEDS)

    def add_item(self, item_list):
        for item in item_list:
            self.item_list[item] = item     # item_list[key=ITEM] : item value

    ## Returns the next item in the item list
    def get_next(self):
        if self.item_index >= len(self.item_list):
            self.item_index = 0
        item, _ = list(self.item_list.items())[self.item_index]
        self.item_index += 1
        print(self.item_index)
        return item

    ## Returns a specified item in the dictionary
    def get(self, item):
        return self.item_list[item]