import sqlite3
from octokit import Octokit
import schedule
import time

def update(nbr, size):
    conn = sqlite3.connect('test_database')
    c = conn.cursor()
    # add row with new commit info
    c.execute('''
              INSERT INTO project (nbrCommits24h, sizeCommits24h)

                    VALUES
                    nbr,
                    size
              ''')

    conn.commit()

class main():
    # timer 24h to run the update function
    # unix time stamp
    octokit = Octokit("api_key")

    a, b = octokit.request("GET /git/rubenbijl/MendixProjectTracking/stats/code_frequency")  # get repository code frequency
    # should be something in this direction

    # somehow this API of github needs to get called once a day, to after store in the database
    update(a, b)

schedule.every(1).day.dp(main)
while 1:
    schedule.run_pending()
    time.sleep(1)