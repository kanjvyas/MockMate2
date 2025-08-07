import sys
import json
import random

def analyze_answer(question, answer):
    # Simple analysis - replace with real AI later
    scores = {
        "confidence": min(9, max(1, len(answer) // 30)) + random.random(),
        "clarity": min(9, max(1, len(answer.split()) // 5)) + random.random(),
        "structure": min(9, max(1, answer.count('.') * 2)) + random.random()
    }
    scores["overall"] = round((scores["confidence"] + scores["clarity"] + scores["structure"]) / 3, 1)
    
    feedback = [
        "Good start! Try to be more specific.",
        "Consider adding quantifiable results.",
        "Connect your answer to the job requirements."
    ]
    
    return {
        "scores": scores,
        "feedback": feedback,
        "sample": "Sample answer would go here..."
    }

if __name__ == "__main__":
    question = sys.argv[1]
    answer = sys.argv[2]
    result = analyze_answer(question, answer)
    print(json.dumps(result))