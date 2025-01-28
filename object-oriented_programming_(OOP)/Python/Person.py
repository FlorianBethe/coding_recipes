# -*- coding: utf-8 -*-
"""
@author: Florian Bethe
"""
import random
from ASCII_Art import ASCII_Art

class Person:
    def __init__(self, gender:str=None):
        genders = ['f', 'm']
        if None == gender:
            self.gender = genders[random.randint(0, 1)]

        elif gender.lower() in ['f', 'm']:
            self.gender = gender.lower()

        else:
            self.gender = genders[random.randint(0, 1)]

        self.name            = None
        self.haircolor       = None
        self.eyecolor        = None
        self.lieblingsessen  = None
        self.bewegungsstatus = None
        self.picture         = ASCII_Art.ASCII_Face(gender)
        
    def __str__(self):
        """
        Dunder-method __str__


        Returns
        -------
        ausgabetext : TYPE
            DESCRIPTION.

        """
        ausgabetext = ""
        ausgabetext += f"Name:            {self.name}\n"
        ausgabetext += f"Hair color:      {self.haircolor}\n"
        ausgabetext += f"Eye color:       {self.eyecolor}\n"
        ausgabetext += f"Lieblingsessen:  {self.lieblingsessen}\n"
        ausgabetext += f"Bewegungsstatus: {self.bewegungsstatus}\n"
        ausgabetext += f"Picture:\n{self.picture}\n"
        return ausgabetext
    
    # Eigenschaften als Liste
    def properties_as_list(self):
        liste = [("Gender",          self.gender),
                 ("Name",            self.name),
                 ("Hair color",      self.haircolor),
                 ("Eyey color",      self.eyecolor),
                 ("Lieblingsessen",  self.lieblingsessen),
                 ("Bewegungsstatus", self.bewegungsstatus),
                 ("Picture",         self.picture)]
        return liste

    

# -------------------------------------------------------------------------- #
# -------------------------------- T E S T ---------------------------------- #
# --------------------------------------------------------------------------- #

if "__main__" == __name__:
    #   Konsole clearen
    #       https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    #       https://hellocoding.de/blog/coding-language/python/farben-im-terminal
    print("\033[H\033[J", end="")       

    persons = []
    for i in range(5):
        persons.append(Person())
        
    for person in persons:
        print(f"\n\n{person.picture}\n\n--------------------------------")
        
    florian = Person()
    
    florian.name            = "Florian Bethe"
    florian.haircolor       = "dark-blond"
    florian.eyecolor        = "blue-grey"
    florian.lieblingsessen  = "Pasta"
    florian.bewegungsstatus = "quite active"
    florian.picture = ASCII_Art.ASCII_Face(gender='m', i=0)

    print(florian)