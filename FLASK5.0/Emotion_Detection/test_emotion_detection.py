import unittest
from unittest.mock import patch
from emotion_detection import emotion_detector

class TestEmotionDetectorMocked(unittest.TestCase):

    @patch('emotion_detection.requests.post')
    def test_mocked_positive_sentiment(self, mock_post):
        # Simulate a successful API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'documentSentiment': {
                'label': 'SENT_POSITIVE',
                'score': 0.95
            }
        }

        result = emotion_detector('I love working with Python')
        self.assertEqual(result['label'], 'SENT_POSITIVE')
        self.assertAlmostEqual(result['score'], 0.95)

    @patch('emotion_detection.requests.post')
    def test_mocked_api_failure(self, mock_post):
        # Simulate a failed API response
        mock_post.return_value.status_code = 500

        with self.assertRaises(ConnectionError):
            emotion_detector('This will fail')

    @patch('emotion_detection.requests.post')
    def test_mocked_invalid_json(self, mock_post):
        # Simulate a malformed response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.side_effect = ValueError("Invalid JSON")

        with self.assertRaises(ValueError):
            emotion_detector('Bad response format')

if __name__ == '__main__':
    unittest.main()