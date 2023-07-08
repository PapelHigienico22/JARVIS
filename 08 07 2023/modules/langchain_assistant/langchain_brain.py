#Comunicarnos con la api de OpenAI
import dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from modules.templates.templates import brain_template

dotenv.load_dotenv()

chat = ChatOpenAI(temperature=0.1)

class LangChainBrainAssistant:
    def chat(self, user_text):
        assistant_prompt = SystemMessagePromptTemplate.from_template(brain_template)
        user_prompt = HumanMessagePromptTemplate.from_template("{user_text}")
        chat_prompt = ChatPromptTemplate.from_messages(
            [assistant_prompt, user_prompt]
        )
        response = chat(chat_prompt.format_prompt(user_text=user_text).to_messages())
        return response