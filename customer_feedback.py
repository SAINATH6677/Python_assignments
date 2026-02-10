def positive_feedback_percentage(ratings):
    if not ratings:
        return 0

    positive = sum(1 for rating in ratings if rating >= 4)
    return (positive / len(ratings)) * 100


# Example usage
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

percentage = positive_feedback_percentage(ratings)
print(f"Positive Feedback: {percentage}%")
