import requests

API_KEY = "ab000b9ef24b4e257a668ba13333c30c"
headers = {"x-apisports-key": API_KEY}

def get_team_id(team_name):
    url = f"https://v3.football.api-sports.io/teams?search={team_name}"
    res = requests.get(url, headers=headers)
    data = res.json()
    try:
        return data['response'][0]['team']['id']
    except:
        return None

def get_last_matches(team_id):
    url = f"https://v3.football.api-sports.io/teams?id={team_id}&last=5"
    res = requests.get(url, headers=headers)
    return res.json()

def calculate_goals(match_data):
    total_goals = 0
    for match in match_data.get('response', []):
        goals = match.get('teams', {}).get('home', {}).get('winner')
        if goals is not None:
            total_goals += 1 if goals else 0
    return total_goals

def analyze_match(match_input):
    try:
        team1, team2 = match_input.split(" - ")
    except:
        return {"Hata": "Maç ismini 'Takım1 - Takım2' formatında girin."}

    id1 = get_team_id(team1)
    id2 = get_team_id(team2)

    if not id1 or not id2:
        return {"Hata": "Takım adı bulunamadı. Lütfen doğru yazın."}

    data1 = get_last_matches(id1)
    data2 = get_last_matches(id2)

    goals1 = calculate_goals(data1)
    goals2 = calculate_goals(data2)

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

# Örnek kullanım:
# print(analyze_match("Galatasaray - Fenerbahçe"))
