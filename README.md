# Question to Concept Mapping Tool

This tool maps questions from various subjects to relevant concepts. It uses a hybrid approach, first attempting to extract concepts using Google's Gemini Pro LLM, and then falling back to a keyword-based search if the LLM approach is unavailable or doesn't yield results.

## Folder Structure

```
.
├── main.py                 # Entry point, handles CLI arguments and orchestrates the process
├── llm_api.py              # Handles Google Gemini API calls, loads API key from .env
├── concept_extractor.py    # Contains the core logic for extracting concepts (both LLM and keyword-based)
├── keyword_dictionary.py   # Defines and provides keyword maps for different subjects
├── csv_reader.py           # Reads CSV data from the resources/ folder
├── resources/              # Folder containing subject-specific CSV files (e.g., ancient_history.csv)
├── .env                    # Stores the Gemini API key (user-created)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Prerequisites

1.  **Python**: Ensure you have Python 3.7+ installed.
2.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your Gemini API Key**:
    *   The tool uses `python-dotenv` to load the API key from a `.env` file.
    *   Create a file named `.env` in the root directory of the project.
    *   Add your Gemini API key to the `.env` file as follows:
        ```
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
    *   If the `GEMINI_API_KEY` is not provided or is invalid, the tool will automatically fall back to the keyword-based extraction method.

## Concept Extraction Process

The tool employs a two-step process for concept extraction:

1.  **LLM-based Extraction (Primary)**:
    *   The `concept_extractor.py` script first attempts to identify concepts using the `call_gemini` function in `llm_api.py`.
    *   It constructs a prompt based on the question and subject and sends it to the Gemini Pro model.
    *   If successful, the LLM returns a comma-separated list of concepts.

2.  **Keyword-based Extraction (Fallback)**:
    *   If the LLM call fails (e.g., API key not configured, network issue, blocked response, or no concepts identified by the LLM), the system automatically falls back to a keyword-based approach.
    *   The `extract_concepts_by_keywords` function in `concept_extractor.py` uses predefined keyword maps relevant to the subject.
    *   These keyword maps are defined in `keyword_dictionary.py` and retrieved using `get_keyword_map(subject)`.
    *   The script then indicates whether the concepts were derived via "LLM" or "Keyword".

## Running the Script

To run the concept extraction process, use the `main.py` script with the `--subject` argument.

```bash
python main.py --subject <subject_name>
```

### Available Subjects

The following subjects are currently supported, based on the keyword maps defined in `keyword_dictionary.py`:

*   `ancient_history`
*   `math`
*   `physics`
*   `economics`

For example, to process questions for Ancient History:
```bash
python main.py --subject ancient_history
```

The output will display each question, the extracted concepts (or "None found"), and the method used for extraction (LLM or Keyword).
---

Feel free to contribute by adding more subjects to `keyword_dictionary.py` or improving the extraction logic.
