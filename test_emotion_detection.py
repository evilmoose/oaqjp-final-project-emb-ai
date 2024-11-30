import unittest
import json
from EmotionDetection.emotion_detection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        statement = "I am glad this happened"
        result = emotion_detection(statement)
        result_dict = json.loads(result)  # Convert JSON string to dictionary
        self.assertEqual(result_dict['dominant_emotion'], 'joy', "Failed for joy")

    def test_anger(self):
        statement = "I am really mad about this"
        result = emotion_detection(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'anger', "Failed for anger")

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detection(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'disgust', "Failed for disgust")

    def test_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detection(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'sadness', "Failed for sadness")

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detection(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'fear', "Failed for fear")

if __name__ == "__main__":
    unittest.main()