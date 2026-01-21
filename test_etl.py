from models import User, Account, Feature, Card, News
from etl import generate_marketing_message


def test_generate_marketing_message():
    user = User(
        name="Teste",
        account=Account("1", "1", 1000, 2000),
        features=[Feature("💳", "Cartão virtual")],
        card=Card("1234", 5000),
        news=[News("🔥", "Promoção especial")]
    )

    message = generate_marketing_message(user)

    assert isinstance(message, str)
    assert "Teste" in message
