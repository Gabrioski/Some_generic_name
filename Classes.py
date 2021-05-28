#Classes

#Baseclass
class Entity:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

#Subclass for locations, used in Planet, Space_station class below.
class Location(Entity): 
    def __init__(self, name, first_description):
        #Call base class constructor
        Entity.__init__(self, name)

        #*Description: Some text related to the location, describing it. This can change, hence
        #multiple descriptions, hence this is a list. Descriptions must NOT be removed from this list.
        #*Locales: Locations that are attached to this particular location (the player can) travel
        #there from this Location.
        #*Event: Special text, player interaction that takes place at a location, sometimes
        #subject to conditions.
        
        self.descriptions = []
        self.locales = []
        self.events = []
        
        #The following variable stores a number that is an index to the list called descriptions.
        #It tells us what description is currently being used for the location. E.g. if it is
        #0 then the first description in the list above is being used. 
        self.current_description_index = 0

        #Push provided first description into our list.
        self.push_description(first_description)


        
    #Add an additional description for this location. 
    def push_description(self, desc):
        self.descriptions.append(desc)

    #Add an additional locale for this location.
    def push_locale(self, locale):
        self.locales.append(locale)
        locale.locales.append(self)
              
    #Add an additional event for this location.
    def push_event(self, event):
        self.events.append(event)

    #Output the locations description
    def get_description(self):
        return self.descriptions[self.current_description_index]

    #Change description index, and hence change the location description
    def change_description(new_index):
        if (len(self.descriptions)-1) >= new_index:
            self.current_description_index = new_index
        else:
            raise Exception("Description wanted does not currently exist! (Location.descriptions does not contain the index requested)")
        #NOTE: stops working if descriptions are removed from self.descriptions

        

#Subclass for the player
class Player(Entity):
    
    #Constructor for Player.
    def __init__(self, name, start_location):

        #Call base class constructor.
        Entity.__init__(self, name)
        
        self.location = start_location

    #Move the player into a new location.
    def move(self, move_location):
        
        #Check if that location is a locale of the players current_location.
        if move_location in self.location.locales:
            self.location = move_location
        else:
            raise Exception("Player cannot move into location not attached to current location they are in! (player.location.locales does not contain move_location.)")
            




    



#subclasss planet, creates planets
class Planet(Location):
    def __init__(self, name, first_description):
        #Call base class constructor
        Location.__init__(self, name, first_description)

#subclass space station, creates space stations
class Space_station(Location):
    def __init__(self, name, first_description):
        #Call base class constructor
        Location._init__(self, name, first_description)













