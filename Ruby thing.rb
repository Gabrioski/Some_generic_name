class Room 
  def initialize(namelocation, description, long_desc) #yeh that's it at the moment 
    @namelocation = namelocation
    @description = description
    @long_desc = long_desc
    @whatdo = 0 #this way the player can choose.
    @linklocations_strings = [] #To compare to player's imput
    @movement = "nil" 
  end
  
  
  def addlink_string(location) # add string to rooms showed to players
    @linklocations_strings.push(location)
  end
    
  def getname_location
    return @namelocation
  end
    
  def add_event(event)
    @events.push(event)
  end
    
  
  def enter_location #Function to use when a player enters a location. 
    until @whatdo == "move"

      puts "You are now inside the #{@namelocation}"
      puts "#{@description}"
      puts "What do you want to do?
            explore
            move"
      @whatdo = gets.to_s.chomp! # this is why I included @whatdo
      if @whatdo == "explore"
        puts @long_desc
              
        clear
      else 
        clear
      end
            
    end
        
     
    until @linklocations_strings.include?(@movement) #loop until imput from the player  == an available option (.include?)
      puts "Where do you want to go?"
      @linklocations_strings.each {|loc| puts loc} #Shows all locations available to player. 
      @movement = gets.chomp!
      clear
      next
    end

    actual_location = @movement
    @movement = "nil"
    @whatdo = 0
    actual_location.to_s
  end

end
