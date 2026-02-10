def calculate_average(marks):
    return sum(marks) / len(marks)


def classroom_performance(students):
    averages = {}
    top_student = None
    highest_avg = 0

    for student, marks in students.items():
        avg = calculate_average(marks)
        averages[student] = round(avg, 2)

        if avg > highest_avg:
            highest_avg = avg
            top_student = student

    return averages, top_student


# Example usage
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages, topper = classroom_performance(students)
print("Average Marks:", averages)
print("Top Performer:", topper)
