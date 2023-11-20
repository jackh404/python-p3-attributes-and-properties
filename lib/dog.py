#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name = "Fido",breed = "Pointer"):
        self.name = name
        self.breed = breed
    def getName (self):
        return self._name
    def getBreed (self):
        return self._breed
    def setName (self, name):
        if(type(name) == str and 1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    def setBreed (self, breed):
        if(breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    name = property(getName, setName)
    breed = property(getBreed, setBreed)
            
#use property()!