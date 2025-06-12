import argparse
from csv_reader import read_subject_csv
from concept_extractor import extract_concepts
from keyword_dictionary import get_keyword_map

# from llm_api import call_anthropic  # Not used, Gemini is called via concept_extractor

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}\n")

    keyword_map = get_keyword_map(args.subject)
    if not keyword_map:
        print(f"Warning: No keyword map found for subject '{args.subject}'. Keyword fallback may not be effective if LLM fails.\n")

    for i, row in enumerate(data):
        question_text = row['Question']
        print(f"Processing Question {i+1}...")

        concepts, method = extract_concepts(question_text, args.subject, keyword_map)

        print(f"Question: {question_text}")
        print(f"Concepts: {', '.join(concepts) if concepts else 'None found'}")
        print(f"Method: {method}")
        print("---")

if __name__ == "__main__":
    main()
