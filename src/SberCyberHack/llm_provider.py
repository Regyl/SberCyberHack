from langchain_community.chat_models import ChatOpenAI


def get_llm():
    return ChatOpenAI(
        base_url="http://localhost:1235/v1",  # LM Studio OpenAI API endpoint
        api_key="lm-studio",  # Dummy key - LM Studio ignores this field, but langchain requires it
        model_name="deepseek-r1"  # Matches the name of the loaded model in LM Studio
    )
