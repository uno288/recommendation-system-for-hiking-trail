import json

# Membaca data dari file mountainDatabases.json
with open("mountainDatabases.json", "r") as file:
    data_jalur_pendakian = json.load(file)


def determine_difficulty(data_jalur_pendakian):
    def mount_difficulty(mountain):
        leveling = 0

        # Analisis berdasarkan ketinggian
        if mountain["ketinggian"] <= 2500:
            leveling += 1
        elif mountain["ketinggian"] <= 3000:
            leveling += 2
        else:
            leveling += 3

        # Analisis berdasarkan jarak tempuh
        jarak_tempuh = (
            float(mountain["jarak_tempuh_km"])
            if isinstance(mountain["jarak_tempuh_km"], (int, float))
            else 10
        )  # Default untuk "Bervariasi"
        if jarak_tempuh <= 5:
            leveling += 1
        elif jarak_tempuh <= 10:
            leveling += 2
        else:
            leveling += 3

        # Analisis berdasarkan estimasi waktu
        estimasi_waktu_min = (
            int(mountain["estimasi_waktu_jam"].split("-")[0])
            if "-" in mountain["estimasi_waktu_jam"]
            else int(mountain["estimasi_waktu_jam"])
        )
        if estimasi_waktu_min <= 5:
            leveling += 1
        elif estimasi_waktu_min <= 8:
            leveling += 2
        else:
            leveling += 3

        # Analisis berdasarkan kondisi jalur
        if (
            "terjal" in mountain["kondisi_jalur"].lower()
            or "menantang" in mountain["kondisi_jalur"].lower()
        ):
            leveling += 3
        elif "beragam" in mountain["kondisi_jalur"].lower():
            leveling += 2
        else:
            leveling += 1

        return leveling

    leveled_mountains = [
        {
            "id": m["id"],
            "nama_gunung": m["nama_gunung"],
            "nama_jalur": m["nama_jalur"],
            "level": mount_difficulty(m),
        }
        for m in data_jalur_pendakian
    ]
    return leveled_mountains


# Menggunakan data jalur pendakian yang diberikan untuk menghitung tingkat kesulitan
tingkat_kesulitan_jalur = determine_difficulty(data_jalur_pendakian)
print(tingkat_kesulitan_jalur)
