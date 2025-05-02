from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest, json

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
    # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        formatted_response = json.loads(result_1)
        self.assertEqual(formatted_response['documentSentiment']['label'], 'SENT_POSITIVE')
    
    # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        formatted_response = json.loads(result_2)
        self.assertEqual(formatted_response['documentSentiment']['label'], 'SENT_NEGATIVE')
    
    # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        formatted_response = json.loads(result_3)
        self.assertEqual(formatted_response['documentSentiment']['label'], 'SENT_NEUTRAL')

unittest.main()