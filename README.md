# Charge-Blade-Dashboard
This is a dashboard for the Charge Blade in the video game Monster Hunter Rise: Sunbreak. I have collected the values for monster hitzones, charge blade motion values, and weapons to calculate the damage on every monster with selected weapons, combos and stats. In a game as daunting as monster hunter, it is helpful to have a visual aid as to how much damage you are dealing at a given point in the game (assuming optimized stats). You get an estimate for how much you should be dealing after beating the first part of the game. 

The project went as follows:
1. Google sheets to collect and clean data
2. Python converting those sheets into databases to be readably by SQLite.
3. SQLite produces the cb_damage sheet with the provided query.
4. use the cb_damage sheet to create the dahsboard.

Overall project took about 1 week with just the sql and tableau part of the project, recycling assets I had available from other projects (the damage calculator) to save time. 
