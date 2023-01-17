from app.schemas.group import Group
from app.schemas.spendings import Spending
from app.schemas.user import Gender, User, UserBase, UserCreate
from app.schemas.wallet import Wallet_types, WalletBase, WalletCreate


def test_user():
    user = User(
        id=1,
        username="username",
        gender=Gender.MALE.value,
        phone_number="+7999123467",
        email="good_email@google.com",
        wallet=1,
        group=1,
    )
    ...
