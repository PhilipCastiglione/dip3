import re

author_re = re.compile(r"^Author")
message_re = re.compile(r"^(?!(Date|Merge|commit))") # not the commit, date, merge hash or an empty line
merge_re = re.compile(r"^Merge ")

def identify(author):
    return {
        'Author: Colin Weight <colin@Colins-Dev-Tool.local>\n': "Colin",
        'Author: Colin Weight <colin.weight@jcurve.com.au>\n': "Colin",
        'Author: Colin Weight <colinweight@users.noreply.github.com>\n': "Colin",
        'Author: Dan Cheail <dan@dnch.io>\n': "Dan",
        'Author: Dan Cheail <dan.cheail@jcurve.com.au>\n': "Dan",
        'Author: Dan Cheail <dan@undumb.com>\n': "Dan",
        'Author: Dan Cheail <dnch@users.noreply.github.com>\n': "Dan",
        'Author: Philip Castiglione <philipcastiglione@gmail.com>\n': "Phil",
        'Author: rudyyazdi <rudyyazdi@gmail.com>\n': "Rudy",
        'Author: Rudy <rudyyazdi@gmail.com>\n': "Rudy"
    }[author]

authors = []
messages = []
with open('log.txt', mode='r', encoding='utf-8') as logfile:
    current_message = ""
    for line in logfile:
        if author_re.match(line):
            if len(authors) > 0:
                messages.append(current_message)
                current_message = ""
            authors.append(line)
        elif message_re.match(line) and len(authors) > 0:
            current_message += line.strip()

    messages.append(current_message)

authors = [identify(author) for author in authors]

results = {}
for idx in range(len(authors)):
    author = authors[idx]
    message = messages[idx]
    if not merge_re.match(message):
        if author in results:
            results[author].append(len(message))
        else:
            results[author] = [len(message)]

summarized_results = {}
for author, commits in results.items():
    fifty_chars = commits.count(50)
    total_commits = len(commits)
    summarized_results[author] = "{:5} of {:5} messages ({:.3f}%) are 50 chars long".format(fifty_chars, total_commits, float(fifty_chars)/total_commits)

for author, result in summarized_results.items():
    print("{:10} {}".format(author, result))
