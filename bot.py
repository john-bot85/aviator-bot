import requests

def get_game_data(game_id):
    url = "https://pakakumi.com/api/v1/games/" + game_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def play_game(game_id, bet_amount):
    data = get_game_data(game_id)
    if data is not None:
        response = requests.post(
            "https://pakakumi.com/api/v1/games/" + game_id + "/play",
            data={"bet_amount": bet_amount}
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    else:
        return None

def main():
    game_id = "123456"
    bet_amount = 100
    game_data = play_game(game_id, bet_amount)
    if game_data is not None:
        print(game_data)

if __name__ == "__main__":
    main()
