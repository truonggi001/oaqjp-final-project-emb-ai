from EmotionDetection import emotion_detector

def test_emotion_detection():
    # List of test cases: (statement, expected_dominant_emotion)
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    ]
    # Run each test case and print the result
    for index, (statement, expected_emotion) in enumerate(test_cases, start=1):
        result = emotion_detector(statement)
        dominant_emotion = result["dominant_emotion"]

        if dominant_emotion == expected_emotion:
            print(f"Test case {index} passed: {dominant_emotion} == {expected_emotion}")
        else:
            print(
                f"Test case {index} FAILED: "
                f"expected {expected_emotion}, got {dominant_emotion}"
            )

if __name__ == "__main__":
    test_emotion_detection()
