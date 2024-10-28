import os
import csv
from collections import defaultdict


our_total_votes = dict()
our_preferences = defaultdict(int)


def find_csv_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                yield file_path


def parse_csv_file(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for index, row in enumerate(reader):
            if index == 0:
                continue
            yield row


for csv_file in find_csv_files("./files"):
    for row in parse_csv_file(csv_file):
        section, vote_type, party, party_total, preference, preference_total = row
        if party == '26':
            our_total_votes[section] = party_total
            our_preferences[preference] += int(preference_total)
