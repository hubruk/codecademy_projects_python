letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "]=0
print(letter_to_points,"\n")

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter.upper()]
  return point_total

brownie_points=score_word("brownie")
print(brownie_points,"\n")

player_to_words = {"player1":	["BLUE","TENNIS","EXIT"],"wordNerd":	["EARTH","EYES","MACHINE"],"Lexi Con":	["ERASER","BELLY","HUSKY"],"Prof Reader": ["ZAP","COMA","PERIOD"]}

def update_point_totals():
  player_to_points = {}
  for key in player_to_words:
    total_player_points = 0
    for value in player_to_words[key]:
      total_player_points += score_word(value)
      player_to_points[key] = total_player_points
  print(player_to_points,"\n")
update_point_totals()

def play_word(player, word):
  little_helper = player_to_words[player]
  little_helper.append(word)
  player_to_words[player]=little_helper

play_word("player1", "BROWNIE")
print(player_to_words,"\n")

update_point_totals()
