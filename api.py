import requests

def get_game_data(game_id):
  response = requests.get(f"https://pakakumi.com/api/games/{game_id}")
  if response.status_code == 200:
    return response.json()
  else:
    return None

def play_game(game_id, bet_amount):
  game_data = get_game_data(game_id)
  if game_data is not None:
    response = requests.post(f"https://pakakumi.com/api/games/{game_id}/play", json={"bet_amount": bet_amount})
    if response.status_code == 200:
      return response.json()
    else:
      return None
  else:
    return None

def main():
  game_id = "123456789"
  bet_amount = 100
  result = play_game(game_id, bet_amount)
  print(result)

if __name__ == "__main__":
  main()
