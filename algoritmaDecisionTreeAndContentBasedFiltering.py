# DECISION TREE ALGORITHM FOR HIKER'S SKILL LEVEL

# Questions and Answers Database
questions = [
    {
        "topic": "Pengalaman Pendakian",
        "questions": [
            {
                "id": 1,
                "text": "Berapa banyak gunung di Jawa yang telah Anda daki?",
                "weight": 0.10,
                "options": [
                    {"label": "0-1 gunung", "value": 1},
                    {"label": "2-4 gunung", "value": 2},
                    {"label": "5 atau lebih gunung", "value": 3},
                ],
            },
            {
                "id": 2,
                "text": "Ketinggian maksimal yang pernah Anda capai dalam pendakian adalah...",
                "weight": 0.10,
                "options": [
                    {"label": "Kurang dari 1.500 meter", "value": 1},
                    {"label": "1.500-3.000 meter", "value": 2},
                    {"label": "Lebih dari 3.000 meter", "value": 3},
                ],
            },
            {
                "id": 3,
                "text": "Jenis jalur pendakian apa yang paling sering Anda lalui?",
                "weight": 0.10,
                "options": [
                    {
                        "label": "Jalur dengan banyak persimpangan dan minim petunjuk",
                        "value": 1,
                    },
                    {
                        "label": "Jalur terjal dengan sedikit bantuan tali atau peralatan",
                        "value": 2,
                    },
                    {"label": "Jalur yang jelas dan terawat dengan baik", "value": 3},
                ],
            },
        ],
    },
    {
        "topic": "Frekuensi Pendakian",
        "questions": [
            {
                "id": 4,
                "text": "Dalam setahun terakhir, berapa kali Anda melakukan pendakian?",
                "weight": 0.10,
                "options": [
                    {"label": "0-1 kali", "value": 1},
                    {"label": "2-5 kali", "value": 2},
                    {"label": "Lebih dari 5 kali", "value": 3},
                ],
            },
        ],
    },
    {
        "topic": "Kondisi Fisik dan Kesehatan",
        "questions": [
            {
                "id": 5,
                "text": "Apakah Anda rutin melakukan latihan fisik untuk mendukung aktivitas pendakian?",
                "weight": 0.10,
                "options": [
                    {"label": "Tidak atau jarang", "value": 1},
                    {"label": "Kadang-kadang, setidaknya seminggu sekali", "value": 2},
                    {"label": "Rutin, beberapa kali seminggu", "value": 3},
                ],
            },
            {
                "id": 6,
                "text": "Apakah Anda memiliki kondisi medis atau fisik yang perlu diperhatikan saat pendakian?",
                "weight": 0.10,
                "options": [
                    {"label": "Ya, ada beberapa keterbatasan", "value": 1},
                    {"label": "Tidak yakin", "value": 2},
                    {"label": "Tidak, saya dalam kondisi fisik prima", "value": 3},
                ],
            },
        ],
    },
    {
        "topic": "Pengetahuan Survival Dasar",
        "questions": [
            {
                "id": 7,
                "text": "Berapa banyak situasi darurat yang Anda tahu cara mengatasinya (misal: badai mendadak, tersesat, cedera)?",
                "weight": 0.15,
                "options": [
                    {"label": "0-2 situasi", "value": 1},
                    {"label": "3-5 situasi", "value": 2},
                    {"label": "Lebih dari 5 situasi", "value": 3},
                ],
            },
        ],
    },
    {
        "topic": "Pengalaman Menggunakan Peralatan Pendakian",
        "questions": [
            {
                "id": 8,
                "text": "Seberapa baik Anda mengenal dan bisa menggunakan peralatan pendakian berikut? (kompas, GPS, pakaian untuk cuaca ekstrem)",
                "weight": 0.15,
                "options": [
                    {"label": "Tidak tahu atau sangat sedikit", "value": 1},
                    {
                        "label": "Tahu dan bisa menggunakan beberapa di antaranya dengan baik",
                        "value": 2,
                    },
                    {
                        "label": "Sangat tahu dan bisa menggunakan semua peralatan tersebut dengan baik",
                        "value": 3,
                    },
                ],
            },
        ],
    },
    {
        "topic": "Kemampuan Navigasi",
        "questions": [
            {
                "id": 9,
                "text": "Apakah Anda bisa membaca peta topografi dan menggunakan kompas dengan benar?",
                "weight": 0.10,
                "options": [
                    {"label": "Tidak tahu atau belum pernah mencoba", "value": 1},
                    {"label": "Bisa dengan bantuan dan praktek", "value": 2},
                    {"label": "Bisa dengan mudah dan akurat", "value": 3},
                ],
            },
        ],
    },
    {
        "topic": "Pengalaman Berkemah",
        "questions": [
            {
                "id": 10,
                "text": "Berapa kali Anda telah berkemah di alam terbuka selama pendakian?",
                "weight": 0.05,
                "options": [
                    {"label": "0-2 kali", "value": 1},
                    {"label": "3-5 kali", "value": 2},
                    {"label": "Lebih dari 5 kali", "value": 3},
                ],
            },
            {
                "id": 11,
                "text": "Seberapa mandiri Anda dalam berkemah? (mendirikan tenda, memasak, manajemen sampah)",
                "weight": 0.05,
                "options": [
                    {
                        "label": "Bergantung pada bantuan orang lain atau panduan",
                        "value": 1,
                    },
                    {
                        "label": "Bisa melakukan kebanyakan tugas dengan sedikit bantuan",
                        "value": 2,
                    },
                    {
                        "label": "Saya bisa mengelola semuanya sendiri dengan efisien",
                        "value": 3,
                    },
                ],
            },
        ],
    },
]


# Function for Calculate Skill Level
def calculate_skill_level(questions, answers):
    total_score = 0
    max_possible_score = 0

    # Iterasi melalui setiap topik dan pertanyaan
    for topic in questions:
        for question in topic["questions"]:
            question_id = question["id"]
            question_weight = question["weight"]
            # Mencari jawaban yang sesuai dengan ID pertanyaan
            answer_value = next(
                (a["value"] for a in answers if a["questionId"] == question_id), 0
            )
            # Menghitung skor untuk pertanyaan ini
            total_score += answer_value * question_weight
            # Menghitung skor maksimal yang mungkin untuk pertanyaan ini
            max_possible_score += (
                3 * question_weight
            )  # Nilai maksimum untuk setiap pilihan adalah 3

    # Menghitung rasio skor
    skill_ratio = total_score / max_possible_score

    # Klasifikasi tingkat kemahiran berdasarkan rasio skor
    if skill_ratio >= 0.7:
        return "expert"
    elif skill_ratio >= 0.4:
        return "intermadiate"
    else:
        return "beginner"


# Contoh jawaban pengguna
example_answers = [
    {"questionId": 1, "value": 3},
    {"questionId": 2, "value": 2},
    {"questionId": 3, "value": 1},
    # Penyesuaian untuk contoh, diasumsikan semua pertanyaan dijawab dengan skema ini
]

# Menghitung tingkat kemahiran berdasarkan contoh jawaban
skill_level = calculate_skill_level(questions, example_answers)

print("Yout Skill Level:", skill_level)
