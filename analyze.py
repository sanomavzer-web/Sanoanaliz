def analiz_et(maç_ismi):
    veri = {
        "Cerro Largo": {"ilk_yarı_gol": [1, 1, 0], "tam_gol": [2, 1, 1]},
        "Montevideo": {"ilk_yarı_gol": [0, 0, 1], "tam_gol": [0, 1, 1]}
    }

    takım1, takım2 = maç_ismi.split(" - ")
    t1 = veri.get(takım1)
    t2 = veri.get(takım2)

    if not t1 or not t2:
        return "Takım verisi bulunamadı."

    ht = "Beraberlik"
    if sum(t1["ilk_yarı_gol"]) > sum(t2["ilk_yarı_gol"]):
        ht = f"{takım1} önde"
    elif sum(t2["ilk_yarı_gol"]) > sum(t1["ilk_yarı_gol"]):
        ht = f"{takım2} önde"

    ft = "Beraberlik"
    if sum(t1["tam_gol"]) > sum(t2["tam_gol"]):
        ft = f"{takım1} kazanır"
    elif sum(t2["tam_gol"]) > sum(t1["tam_gol"]):
        ft = f"{takım2} kazanır"

    return {
        "HT Tahmini": ht,
        "FT Tahmini": ft,
        "Güven Skoru": "%75",
        "Bahis Önerisi": f"HT/FT: {ht.split()[0][0]}/{ft.split()[0][0]} – FT: {ft.split()[0][0]}"
    }
