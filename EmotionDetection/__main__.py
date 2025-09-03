"""
Main module for EmotionDetection package.
Allows running the package as: python -m EmotionDetection
"""

from .emotion_detection import emotion_detector
import sys


def main():
    """Main function to run emotion detection from command line."""
    if len(sys.argv) > 1:
        # Join all arguments as the text to analyze
        text = " ".join(sys.argv[1:])
        result = emotion_detector(text)
        
        print(f"\nText: '{text}'")
        print("\nEmotion Analysis:")
        print(f"  Anger:    {result['anger']:.3f}")
        print(f"  Disgust:  {result['disgust']:.3f}")
        print(f"  Fear:     {result['fear']:.3f}")
        print(f"  Joy:      {result['joy']:.3f}")
        print(f"  Sadness:  {result['sadness']:.3f}")
        print(f"\nDominant Emotion: {result['dominant_emotion'].upper()}")


if __name__ == "__main__":
    main()