import requests

API_KEY = "OnurMavZer75"
headers = {"x-apisports-key": OnurMavZer75}

def get_team_id(team_name):
    url = f"https://v3.football.api-sports.io/teams?search={team_name}"
    res = requests.get(url, headers=headers)
    data = res.json()
    return data['response'][0]['team']['id']

def get_last_matches(team_id):
    url = f"https://v3.football.api-sports.io/teams/{team_id}/fixtures?last=5"
    res = requests.get(url, headers=headers)
    return res.json()

def analyze_match(team1, team2):
    id1 = get_team_id(team1)
    id2 = get_team_id(team2)
    data1 = get_last_matches(id1)
    data2 = get_last_matches(id2)

    # Basit analiz mantığı (örnek)
    goals1 = sum([m['goals']['for']['total'] for m in data1['response']])
    goals2 = sum([m['goals']['for']['total'] for m in data2['response']])

    ht = "Beraberlik"
    ft = "Beraberlik"
    if goals1 > goals2:
        ht = f"{team1} önde"
        ft = f"{team1} kazanır"
    elif goals2 > goals1:
        ht = f"{team2} önde"
        ft = f"{team2} kazanır"

    return {
        "HT Tahmini": ht,
        "FT Tahmini": ft,
        "Güven Skoru": "%78",
        "Bahis Önerisi": f"HT/FT: {ht.split()[0][0]}/{ft.split()[0][0]} – FT: {ft.split()[0][0]}"
    }
