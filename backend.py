import os
import certifi
import operator
import uuid
import psycopg
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from psycopg.rows import dict_row
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import (
    AnyMessage,
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain_groq import ChatGroq
from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights




load_dotenv()


os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()



def get_database_url():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is missing. Please add your Render PostgreSQL External Database URL to .env"
        )

    if "sslmode=" not in database_url:
        separator = "&" if "?" in database_url else "?"
        database_url = f"{database_url}{separator}sslmode=require"

    return database_url

GORQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GORQ_API_KEY:
    raise ValueError("GORQ_API_KEY is Missing.Please add it to your .env file")


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)



