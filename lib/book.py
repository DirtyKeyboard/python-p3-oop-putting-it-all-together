#!/usr/bin/env python3
import ipdb
class Book:
    def __init__(self, title='Nothing', author='Nobody', genre="None"):
        self.title = title
        self.author = author
        self._page_count = 0
        self.genre = genre

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print('page_count must be an integer')
    
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

#ipdb.set_trace()