#!/usr/bin/env python3

def top_students(mongo_collection):
    students = list(mongo_collection.find())

    for student in students:
        scores = student.get("scores", [])
        average_score = sum(score.get("score", 0)
                            for score in scores) / len(scores)
        student["averageScore"] = average_score

    def get_average_score(student):
        return student["averageScore"]

    return sorted(students, key=get_average_score, reverse=True)
