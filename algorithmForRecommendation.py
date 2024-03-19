import json


# Load Data from JSON file
def load_questions_and_answers(filename="questionsAndAnswersDatabase.json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["allQuestions"]


with open("mountainDatabase.json", "r") as file:
    trailData = json.load(file)


# Algorithm for Determine Hiker's Skill Level
def calculateSkillLevel(questions, answers):
    total_score = 0
    maxPossibleScore = 0

    # Iterate through each topic and question
    for topic in questions:
        for question in topic["questions"]:
            questionId = question["id"]
            questionWeight = question["weight"]
            # Look for answers that match the question ID
            answerValue = next(
                (a["value"] for a in answers if a["questionId"] == questionId), 0
            )
            # Calculate the score for this question
            total_score += answerValue * questionWeight
            # Calculate the maximum possible score for this question
            maxPossibleScore += 3 * questionWeight

    # Calculates the score ratio
    skillRatio = total_score / maxPossibleScore

    # Classification of proficiency levels based on score ratio
    if skillRatio >= 0.8:
        return "expert"
    elif skillRatio >= 0.5:
        return "intermadiate"
    else:
        return "beginner"


# Algorithms for Define Mountain Difficulties
def determine_difficulty(trailData):
    def mount_difficulty(mountain):
        score = 0

        # Analysis based on elevation
        if mountain["ketinggian"] <= 2500:
            score += 1
        elif mountain["ketinggian"] <= 3000:
            score += 2
        else:
            score += 3

        # Analysis based on distance
        distance = (
            float(mountain["jarak_tempuh_km"])
            if isinstance(mountain["jarak_tempuh_km"], (int, float))
            else 7
        )  # Default for non-defined distance
        if distance <= 5:
            score += 1
        elif distance <= 10:
            score += 2
        else:
            score += 3

        # Analysis based on time estimation
        estimatedTime = (
            int(mountain["estimasi_waktu_jam"].split("-")[0])
            if "-" in mountain["estimasi_waktu_jam"]
            else int(mountain["estimasi_waktu_jam"])
        )
        if estimatedTime <= 5:
            score += 1
        elif estimatedTime <= 8:
            score += 2
        else:
            score += 3

        # Analysis based on path conditions
        if (
            "terjal" in mountain["kondisi_jalur"].lower()
            or "menantang" in mountain["kondisi_jalur"].lower()
        ):
            score += 3
        elif "beragam" in mountain["kondisi_jalur"].lower():
            score += 2
        else:
            score += 1
        return score

    result = [
        {
            "id": m["id"],
            "nama_gunung": m["nama_gunung"],
            "nama_jalur": m["nama_jalur"],
            "totalScore": mount_difficulty(m),
        }
        for m in trailData
    ]
    return result


# Algorithms for Make Recommendation Trails
def recommend_trails(skillLevel, mountainScore):
    if skillLevel == "beginner":
        recommended_trails = [
            mountain for mountain in mountainScore if mountain["totalScore"] <= 7
        ]
    elif skillLevel == "intermadiate":
        recommended_trails = [
            mountain for mountain in mountainScore if 7 < mountain["totalScore"] <= 10
        ]
    elif skillLevel == "expert":
        recommended_trails = [
            mountain for mountain in mountainScore if mountain["totalScore"] > 10
        ]
    else:
        recommended_trails = []

    return recommended_trails


if __name__ == "__main__":
    # example answers from user
    example_answers = [
        {"questionId": 1, "value": 2},
        {"questionId": 2, "value": 2},
        {"questionId": 3, "value": 2},
        {"questionId": 4, "value": 2},
        {"questionId": 5, "value": 2},
        {"questionId": 6, "value": 2},
        {"questionId": 7, "value": 2},
        {"questionId": 8, "value": 2},
        {"questionId": 9, "value": 2},
        {"questionId": 10, "value": 2},
        {"questionId": 11, "value": 2},
    ]

    mountainScoreResult = determine_difficulty(trailData)
    # print(mountainScoreResult)

    questions = load_questions_and_answers()
    skillLevel = calculateSkillLevel(questions, example_answers)
    print("Your Skill Level:", skillLevel)

    # Mendapatkan rekomendasi berdasarkan tingkat kemahiran
    recommended_trails = recommend_trails(skillLevel, mountainScoreResult)

    # Cetak rekomendasi
    for trail in recommended_trails:
        print(
            f"Nama Gunung: {trail['nama_gunung']}, Nama Jalur: {trail['nama_jalur']}, Tingkat Kesulitan: {trail['totalScore']}"
        )
