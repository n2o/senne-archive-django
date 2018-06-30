import os
from typing import List

from archive.models import Author, Item


def get_author_by_lastname(lastname):
    myauthors = Author.objects.filter(lastname__icontains=lastname)
    if len(myauthors) == 1:
        return myauthors[0]


def assign_authors_to_items(author, items):
    for item in items:
        item.author = author
        item.save()


def get_items_by_authors_lastname(lastname):
    return Item.objects.filter(author__icontains=lastname)


def get_all_authors_sorted():
    return list(Author.objects.all())


def get_all_used_authors_by_lastname_in_items():
    return sorted([item.author for item in Item.objects.all()])


# -----------------------------------------------------------------------------

def assign_author_by_lastname_to_items(lastname):
    author = get_author_by_lastname(lastname)
    items = get_items_by_authors_lastname(lastname)
    if not author:
        return "AUTHOR NOT FOUND"
    if not items:
        return "ITEMS NOT FOUND"
    assign_authors_to_items(author, items)


# -----------------------------------------------------------------------------

def move_old_file_to_new_directory(item: Item, author: Author, new_filepath):
    old_filepath = item.file1.name
    new_file_directory = "media/archive/" + author.filepath
    if not os.path.exists("media/archive/" + author.filepath):
        os.makedirs(new_file_directory)
    os.rename("media/" + old_filepath, "media/" + new_filepath)


def update_file_path(item):
    if item and item.file1 and item.author:
        print(item)
        filepath: List[str] = item.file1.name.split("/")
        new_filepath = construct_new_filepath(filepath, item)
        item.file1.name = new_filepath
        item.save()


def construct_new_filepath(filepath, item):
    del filepath[1]  # remove old author-path
    filepath.insert(1, item.author.filepath)
    return "/".join(filepath)


def create_folder_by_author(author: Author):
    new_file_directory = "media/archive/" + author.filepath
    if not os.path.exists(new_file_directory):
        os.makedirs(new_file_directory)
