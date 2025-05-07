"""Simulate a turtle race"""

from race_master import RaceMaster

if __name__ == "__main__":
    racers = ["yellow", "blue", "pink", "orange", "black", "brown"]
    # Create racers and put them in their positions
    tanya = RaceMaster(racers)
    # Start race
    tanya.begin_race()
    # Declare the winners
    tanya.announce()
