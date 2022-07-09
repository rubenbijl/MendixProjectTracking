# MendixProjectTracking

In this project a sample idea is created how to track open-source project(s). As basis the liveliness of a project is stored in a Python SQL database with 2 components, updated per day and a total of these two components per project.

To track the liveliness of a opensource project two components are considered: 
- the amount of commits
- the size of the commits

To update the database once a day the scripts gets the commit info from the project(s) repository.
