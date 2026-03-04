# Citation: IBM. (2024). IBM watsonx.ai Python SDK Documentation.
# https://ibm.github.io/watsonx-ai-python-sdk/index.html
# Citation: IBM. (2024). Foundation Models - ModelInference class.
# https://ibm.github.io/watsonx-ai-python-sdk/foundation_models.html#modelinference

from ibm_watsonx_ai.foundation_models import ModelInference
from app.core.config import settings

def get_watson_model():
    #srart the inference engine
    credentials = {
        "url": settings.WATSONX_URL,
        "apikey": settings.WATSONX_API_KEY
    }
    
    # Using ModelInference
    model = ModelInference(
        model_id=settings.WATSONX_MODEL_ID,
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 500,
            "min_new_tokens": 1
        },
        credentials=credentials,
        project_id=settings.WATSONX_PROJECT_ID
    )
    return model

def ask_watson(prompt: str) -> str:
    #send prompt to watson
    model = get_watson_model()
    # .generate_text() returns the raw string response
    response = model.generate_text(prompt)
    return response
