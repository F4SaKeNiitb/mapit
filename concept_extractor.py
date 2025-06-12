from llm_api import call_gemini

def extract_concepts_by_keywords(question: str, keyword_map: dict) -> list[str]:
    """
    Extracts concepts from a question based on a keyword map.
    """
    question_lower = question.lower()
    found_concepts = set()
    for keyword, concept in keyword_map.items():
        if keyword in question_lower:
            found_concepts.add(concept)
    return list(found_concepts)

def extract_concepts_with_llm(question: str, subject: str) -> list[str]:
    """
    Extracts concepts from a question using an LLM.
    """
    prompt = f"Identify the key concepts tested in the following competitive exam question on the subject of {subject}. List only the concepts, separated by commas. Question: {question}"
    response = call_gemini(prompt)

    # Check for various error responses or empty response
    if not response or \
       response.startswith("An error occurred:") or \
       response.startswith("Request blocked due to:") or \
       response.startswith("No content generated.") or \
       response.startswith("Error: GEMINI_API_KEY not configured."):
        return []

    # Proceed with parsing only if the response seems valid
    concepts = [concept.strip() for concept in response.split(',') if concept.strip()]
    return concepts

def extract_concepts(question: str, subject: str, keyword_map: dict) -> tuple[list[str], str]:
    """
    Extracts concepts using LLM first, then falls back to keywords.
    """
    llm_concepts = extract_concepts_with_llm(question, subject)
    if llm_concepts:
        return llm_concepts, "LLM"

    keyword_concepts = extract_concepts_by_keywords(question, keyword_map)
    return keyword_concepts, "Keyword"
