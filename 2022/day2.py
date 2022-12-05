#### Day 2: Rock Paper Scissors

## Part 1, calculate game total

# Read in game file
input_file = open("./day2_input.txt", "r")
game_input = input_file.read()

# Turn into a list
game_list = list(game_input.split("\n"))

# Initialize score as 0
score = 0

for i in game_list:
    for opponent in i[0]:
        for self in i[2]:
            
            # Sum points based on shape (rock, paper, scissors)
            # Rock
            if self == "X":
                score += 1
            # Paper
            if self == "Y":
                score += 2
            # Scissors
            if self == "Z":
                score += 3
            
            # Sum points based on game outcome (draw or win--losses don't need to be summed because score is 0)
            # Draw
            # Both rock
            if opponent == "A" and self == "X":
                score += 3
            # Both paper
            if opponent == "B" and self == "Y":
                score += 3
            # Both scissors
            if opponent == "C" and self == "Z":
                score += 3
            # Win
            # Opponent = rock, self = paper
            if opponent == "A" and self == "Y":
                score += 6
            # Opponent = paper, self = scissors
            if opponent == "B" and self == "Z":
                score += 6
            # Opponent = scissors, self = rock
            if opponent == "C" and self == "X":
                score += 6

print("Score is:", score, "points.")

## Part 2, calculate game total with new strategy

# Initialize score as 0
score = 0

for i in game_list:
    for opponent in i[0]:
        for self in i[2]:
            
            # Sum points based on game outcome (loss, draw, win), which determines shape (rock, paper, scissors)
            # Loss
            if self == "X":
                score += 0
                # Opponent = rock
                if opponent == "A":
                    # Self = scissors
                    score += 3
                # Opponent = paper
                if opponent == "B":
                    # Self = rock
                    score += 1
                # Opponent = scissors
                if opponent == "C":
                    # Self = paper
                    score += 2 
            # Draw
            if self == "Y":
                score += 3
                # Opponent = rock
                if opponent == "A":
                    # Self = rock
                    score += 1
                # Opponent = paper
                if opponent == "B":
                    # Self = paper
                    score += 2
                # Opponent = scissors
                if opponent == "C":
                    # Self = scissors
                    score += 3
            # Win
            if self == "Z":
                score += 6
                # Opponent = rock
                if opponent == "A":
                    # Self = paper
                    score += 2
                # Opponent = paper
                if opponent == "B":
                    # Self = scissors
                    score += 3
                # Opponent = scissors
                if opponent == "C":
                    # Self = rock
                    score += 1

print("Score is:", score, "points.")

# Close input file
input_file.close()
