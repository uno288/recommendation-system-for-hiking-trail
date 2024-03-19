# Mendefinisikan ulang data jalur pendakian dan fungsi untuk menghitung tingkat kesulitan
data_jalur_pendakian = [
    {
        "nama_gunung": "Gunung Gede",
        "nama_jalur": "Cibodas",
        "lokasi": "Cibodas, Jawa Barat",
        "ketinggian": 2958,
        "jarak_tempuh_km": 7,
        "estimasi_waktu_jam": "6-8",
        "kondisi_jalur": "Beragam, mulai dari hutan hujan tropis hingga area berbatu",
        "aksesibilitas_fasilitas": "Tersedia pos pendaftaran, pos peristirahatan, sumber air, dan shelter",
        "deskripsi": "Populer di kalangan pendaki pemula dan menengah, menawarkan pemandangan alam yang menakjubkan.",
    },
    # Data lainnya disederhanakan untuk fokus pada implementasi
]


def determine_difficulty(data_jalur_pendakian):
    def calculate_leveling(mountain):
        leveling = 0

        # Analisis berdasarkan ketinggian
        if mountain["ketinggian"] <= 2000:
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
            "nama_gunung": mountain["nama_gunung"],
            "nama_jalur": mountain["nama_jalur"],
            "level": calculate_leveling(mountain),
        }
        for mountain in data_jalur_pendakian
    ]
    return leveled_mountains


# Menggunakan data jalur pendakian yang diberikan untuk menghitung tingkat kesulitan
leveled_mountains = determine_difficulty(data_jalur_pendakian)

for mountain in leveled_mountains:
    print(
        f"Gunung: {mountain['nama_gunung']}, Jalur: {mountain['nama_jalur']}, Tingkat Kesulitan: {mountain['level']}"
    )
