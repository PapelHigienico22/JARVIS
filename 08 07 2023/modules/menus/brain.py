from modules.talker.talk import Talker, TtsTalker
# from modules.talker.talk import Talker, FakeYouTalker
from modules.listen import Listener
from modules.notion.notion_integration import Notion
from modules.langchain_assistant.langchain_brain import LangChainBrainAssistant


talker = Talker(TtsTalker())
# talker = Talker(FakeYouTalker('Pancitou', 'papu2273', 'Toretto'))
listener = Listener()
langchain_assistant = LangChainBrainAssistant()
notion = Notion()

# # Nos saluda
# def say_welcome():
#     talker.talk(
#         "Hola señor, me alegra volver a verlo."
#         " ¿De qué tema le gustaría saber?"
#     )

# Nos escucha
def listen_to_response():
    return listener.listen()

# Genera la respuesta
def generate_response():
    response = langchain_assistant.chat(listen_to_response())
    return eval(response.content)

def create_notion_page(data):
    properties = {
        "Name": {"title": [{"text": {"content": f"{data.get('title', None)}"}}]},
        }
    children_page = [{"object": "block", "paragraph":{"rich_text":[{"text":{"content":f"{data.get('content', None)}"}}]}}]
    notion.create_page(properties=properties, children=children_page)

# Nos responde con el modelo de voz
def start_brain_mode():
    talker.say_welcome()
    assistant_response = generate_response()
    print(assistant_response.get('content', None))
    talker.talk(assistant_response.get('content', None))
    create_notion_page(assistant_response)
    