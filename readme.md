# Fine-Tuning Cohere Model and Sentiment Analysis Chatbot

This project demonstrates how to fine-tune a Cohere model for text classification and set up a chatbot to analyze the sentiment of financial text using the Django framework.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Chatbot

1. Set up your Cohere API key:
    - Replace `"COHERE_API_KEY"` in `views.py` within the `sentiment_analysis` app with your actual Cohere API key.

2. Add fine tuned model id in `views.py`:
    ```python
    from django.http import JsonResponse
    import cohere

    def analyze_sentiment(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            text = data.get('text')
            co = cohere.Client('COHERE_API_KEY')
            response = co.classify(
                model='your-fine-tuned-model-id',
                inputs=[text]
            )
            sentiment = response.classifications[0].prediction
            return JsonResponse({'sentiment': sentiment})
    ```

3. Run the Django server:
    ```sh
    python manage.py runserver
    ```

4. Go to http://127.0.0.1:8000/ and test it out!

## Fine-Tuning

1. Set up your Cohere API key:
    - Replace `"COHERE_KEY"` in `fine_tuning.py` with your actual Cohere API key.

2. Prepare your dataset:
    - Ensure your dataset is in CSV format with columns `query` and `sentiment`.
    - Update the path to your dataset in `fine_tuning.py`:
        ```python
        df = pd.read_csv('<path-to-your-dataset>', names=['query', 'sentiment'])
        ```

3. Fine tune the model on Cohere or Run the script to create the JSONL file for fine-tuning:
    ```sh
    python fine_tuning.py
    ```
