'''
Provides template code to automatically make decisions for the autonomous
car.
'''
from scenario import Scenario

def decide(scenario):
    """ Decides whether your car will save the passengers or pedestrians

    Args:
        scenario: a Scenario object defined in scenario.py. This object contains
            all of the information about the scenario. You can see some
            examples below in the sample code.

    Returns:
        A string indicating whether you are saving "passengers" or
        "pedestrians". Note that your method MUST make a decision for
        ANY potential scenario.
    """

    # NOTE: YOU NEED TO REPLACE ALL OF THE CODE BELOW!!!
    # This simply demonstrates how to access information from the scenario.
    # print("Are the pedestrians crossing legally?", scenario.legalCrossing)
    # print("Is the car in the same lane as the pedestrians?", scenario.pedsInLane)
    # print("Are you in car?", scenario.youInCar)
    #
    # print("Print whether each pedestrian is a human, animal, or you")
    # for person in scenario.pedestrians:
    #     print(person.charType)


    # Your program must choose to save either pedestrians or passengers.
    # This is an overly simple rule that only saves the passengers if there are
    # more passengers than pedestrians.

   
    # else:
    #     return "pedestrians"
    
    # if len(scenario.passengers) > len(scenario.pedestrians):
    #     return "passengers"
    
    pedestrianAnimalCount=0
    passengerHumanCount=0
    pedestrialAnimalCount=0
    # I prioritize legal crossing over any other factor.(I prioritize the law over sentiments but there are exceptions such as if its an animals)
    if scenario.legalCrossing:
       
        # If the passengers are way greater than the pedestrians then save the passengers even though it's a legal crossing because it would rarely happen and it would do the world a greater good. 
        if len(scenario.passengers) > len(scenario.pedestrians)+100:
            return "passengers"
        
        # Save the pedestrians regardless if they are crossing legally or not as long as all the passengers are animals.
        for person in scenario.pedestrians:
            if person.charType=="human":
                pedestrialAnimalCount+=1
        for person in scenario.passengers:
            if person.charType=="human":
                passengerHumanCount+=1
        if pedestrianAnimalCount==0:
            if passengerHumanCount>0:
                return "passengers"


        # if scenario.pedsInLane:
        #     return "pedestrians"
        return "pedestrians"
    else:
           
        # If the pedestrians are way greater than the passengers then save the pedestrians even though it's an illegal crossing because it would rarely happen and it would do the world a greater good. 
        if len(scenario.pedestrians) > len(scenario.passengers)+100:
            return "pedestrians"
        
          # Checks if the pedestrians crossing illegally are only animals and if they are only animals then check if the passenger has at least one human.
        for person in scenario.passengers:
            if person.charType=="human":
                passengerHumanCount+=1
        for person in scenario.pedestrians:
            if person.charType=="human":
                pedestrianAnimalCount+=1
        
        if passengerHumanCount==0:
            if pedestrialAnimalCount>0:
                return "pedestrians"

    

        return "passengers"
