import streamlit as st
from langchain_openai import OpenAI
from langchain import PromptTemplate

st.set_page_config(
    page_title = "Generador de entradas de blog"
)

st.title("Generador de entradas de blog")

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type = "password"
)

def generate_response(topic):
    llm = OpenAI(openai_api_key=openai_api_key)
    template = """
    Como escritor con experiencia en creación de contenido, 
    genera una entrada de blog de 400 palabras sobre {topic}
    
    Tu respuesta debe tener este formato:
    Primero, imprime la entrada del blog.
    A continuación, suma el número total de palabras que contiene e imprime el resultado de esta forma: Este post tiene X palabras.
    """
    prompt = PromptTemplate(
        input_variables = ["topic"],
        template = template
    )
    query = prompt.format(topic=topic)
    response = llm(query, max_tokens=2048)
    return st.write(response)

st.write("Contacte con [Matias Toro Labra](https://www.linkedin.com/in/luis-matias-toro-labra-b4074121b/) para construir sus proyectos de IA")

topic_text = st.text_input("Introducir tema: ")
if not openai_api_key.startswith("sk-"):
    st.warning("Enter OpenAI API Key")
if openai_api_key.startswith("sk-"):
    generate_response(topic_text)
        
