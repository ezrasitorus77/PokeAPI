import requests

pokemon = input("Masukkan nama / id pokemon : ").lower()
req = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)

while req.status_code == 404: # menandakan query user tidak ditemukan di API
    pokemon = input("Nama / id pokemon yang Anda masukkan tidak terdaftar. Silahkan ulangi memberi masukkan : ").lower()
    req = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)

if req.status_code == 200: # akses berhasil didapat
    req = req.json()
    print(f'''Name : {req["forms"][0]["name"].capitalize()}
HP : {req["stats"][0]["base_stat"]}
Attack : {req["stats"][1]["base_stat"]}
Defense : {req["stats"][2]["base_stat"]}
Speed : {req["stats"][-1]["base_stat"]}
Type : {req["types"][0]["type"]["name"].capitalize()}''')
    print("Ability :")
    for i, v in enumerate(req["abilities"]): # index diperlukan untuk memberi nomor pada cetakan
        print(f"{i + 1}. {v['ability']['name'].capitalize().replace('-', ' - ')}")

else: # jika status code diluar 200 atau 404, misal 502 Bad Gateway, maka diasumsikan terjadi kesalahan jaringan
    print("Terjadi kesalahan pada jaringan. Silahkan ulangi kembali dalam beberapa waktu atau hubungi penyedia layanan.")