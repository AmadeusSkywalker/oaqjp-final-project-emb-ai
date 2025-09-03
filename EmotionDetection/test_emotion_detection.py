"""
Unit tests for the EmotionDetection package.

This module tests the emotion_detector function with various statements
to verify that it correctly identifies the dominant emotion.
"""

import unittest

from .emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""
    
    def setUp(self):
        """Set up test cases with statements and expected dominant emotions."""
        self.test_cases = [
            {
                "statement": "I am glad this happened",
                "expected_emotion": "joy",
                "test_name": "test_joy_emotion"
            },
            {
                "statement": "I am really mad about this",
                "expected_emotion": "anger",
                "test_name": "test_anger_emotion"
            },
            {
                "statement": "I feel disgusted just hearing about this",
                "expected_emotion": "disgust",
                "test_name": "test_disgust_emotion"
            },
            {
                "statement": "I am so sad about this",
                "expected_emotion": "sadness",
                "test_name": "test_sadness_emotion"
            },
            {
                "statement": "I am really afraid that this will happen",
                "expected_emotion": "fear",
                "test_name": "test_fear_emotion"
            }
        ]
    
    def test_joy_emotion(self):
        """Test that 'I am glad this happened' returns joy as dominant emotion."""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        self.assertEqual(result['dominant_emotion'], 'joy', 
                        f"Expected 'joy' but got '{result['dominant_emotion']}' for statement: {statement}")
        
        # Verify all emotion scores are present
        expected_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in expected_keys:
            self.assertIn(key, result, f"Result should contain '{key}' key")
    
    def test_anger_emotion(self):
        """Test that 'I am really mad about this' returns anger as dominant emotion."""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertEqual(result['dominant_emotion'], 'anger',
                        f"Expected 'anger' but got '{result['dominant_emotion']}' for statement: {statement}")
    
    def test_disgust_emotion(self):
        """Test that 'I feel disgusted just hearing about this' returns disgust as dominant emotion."""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertEqual(result['dominant_emotion'], 'disgust',
                        f"Expected 'disgust' but got '{result['dominant_emotion']}' for statement: {statement}")
    
    def test_sadness_emotion(self):
        """Test that 'I am so sad about this' returns sadness as dominant emotion."""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertEqual(result['dominant_emotion'], 'sadness',
                        f"Expected 'sadness' but got '{result['dominant_emotion']}' for statement: {statement}")
    
    def test_fear_emotion(self):
        """Test that 'I am really afraid that this will happen' returns fear as dominant emotion."""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertEqual(result['dominant_emotion'], 'fear',
                        f"Expected 'fear' but got '{result['dominant_emotion']}' for statement: {statement}")
    
    def test_response_format(self):
        """Test that the response has the correct format and all required fields."""
        statement = "Test statement for format verification"
        result = emotion_detector(statement)
        
        # Check that result is a dictionary
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        
        # Check all required keys are present
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result, f"Result should contain '{key}' key")
        
        # Check that emotion scores are numeric
        emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for key in emotion_keys:
            self.assertIsInstance(result[key], (int, float), 
                                f"'{key}' value should be numeric")
            self.assertGreaterEqual(result[key], 0, 
                                  f"'{key}' value should be non-negative")
            self.assertLessEqual(result[key], 1, 
                               f"'{key}' value should not exceed 1")
        
        # Check that dominant_emotion is a string
        self.assertIsInstance(result['dominant_emotion'], str, 
                            "'dominant_emotion' should be a string")
        
        # Check that dominant_emotion is one of the valid emotions
        valid_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        self.assertIn(result['dominant_emotion'], valid_emotions,
                     f"'dominant_emotion' should be one of {valid_emotions}")
    
    def test_all_statements_summary(self):
        """Run all test statements and print a summary."""
        print("\n" + "="*70)
        print("EMOTION DETECTION TEST SUMMARY")
        print("="*70)
        print(f"{'Statement':<45} {'Expected':<10} {'Actual':<10} {'Pass':<5}")
        print("-"*70)
        
        all_passed = True
        for test_case in self.test_cases:
            statement = test_case['statement']
            expected = test_case['expected_emotion']
            
            try:
                result = emotion_detector(statement)
                actual = result['dominant_emotion']
                passed = actual == expected
                all_passed = all_passed and passed
                
                print(f"{statement:<45} {expected:<10} {actual:<10} {'✓' if passed else '✗':<5}")
            except Exception as e:
                print(f"{statement:<45} {expected:<10} {'ERROR':<10} {'✗':<5}")
                print(f"  Error: {str(e)}")
                all_passed = False
        
        print("="*70)
        print(f"Overall Result: {'ALL TESTS PASSED ✓' if all_passed else 'SOME TESTS FAILED ✗'}")
        print("="*70 + "\n")


if __name__ == '__main__':
    # Run the unit tests with verbose output
    print("Running EmotionDetection Unit Tests...")
    print("-" * 70)
    
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEmotionDetection)
    
    # Run the tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    print("="*70)
