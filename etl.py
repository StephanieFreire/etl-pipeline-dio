import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

from models import User, Account, Feature, Card, News

# Carrega variáveis de ambiente
load_dotenv()

# Cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =========================
# EXTRAÇÃO
# =========================
def extract_user_ids(csv_path):
    """
    Extrai os IDs dos usuários a partir de um arquivo CSV
    """
    df = pd.read_csv(csv_path)
    return df["user_id"].tolist()


def extract_user_data(user_id):
    """
    Simula a extração de dados de uma API externa
    """
    account = Account(
        number="123456",
        agency="0001",
        balance=2500.00 + user_id,
        limit=4000.00
    )

    features = [
        Feature(icon="💳", description="Cartão virtual"),
        Feature(icon="📱", description="Aplicativo Santander")
    ]

    card = Card(
        number="**** **** **** 1234",
        limit=8000.00
    )

    news = [
        News(icon="🔥", description="Novo limite disponível para você!")
    ]

    return User(
        name=f"Usuário {user_id}",
        account=account,
        features=features,
        card=card,
        news=news
    )


# =========================
# TRANSFORMAÇÃO (IA)
# =========================
def generate_marketing_message(user: User):
    """
    Gera uma mensagem personalizada utilizando IA (OpenAI GPT)
    """
    prompt = f"""
    Crie uma mensagem curta e amigável de marketing para um cliente bancário.

    Nome: {user.name}
    Saldo: {user.account.balance}
    Limite do cartão: {user.card.limit}
    Funcionalidades: {[f.description for f in user.features]}
    Novidade: {user.news[0].description}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# =========================
# CARREGAMENTO
# =========================
def load_message(user_id, message):
    """
    Simula o carregamento dos dados em um sistema externo
    """
    print("\n📤 Mensagem enviada:")
    print({
        "userId": user_id,
        "message": message
    })


# =========================
# EXECUÇÃO DO ETL
# =========================
def run_etl():
    user_ids = extract_user_ids("data/users.csv")

    for user_id in user_ids:
        user = extract_user_data(user_id)
        message = generate_marketing_message(user)
        load_message(user_id, message)


if __name__ == "__main__":
    run_etl()
