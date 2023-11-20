#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="Bob",job="Builder"):
        self.name = name
        self.job = job
    def setName(self,name):
        if(type(name)==str and 1 <= len(name) <= 25):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    def setJob(self,job):
        if(job in APPROVED_JOBS):
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    def getName(self):
        return self._name
    def getJob(self):
        return self._job
    name = property(getName, setName)
    job = property(getJob, setJob)
