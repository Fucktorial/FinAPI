from pydantic import BaseModel


class WalletBase(BaseModel):
    id_type: int
    name: str(max_lenght=30)


class Wallet_types(BaseModel):
    id: int
    name: str(max_lenght=30)


class WalletCreate(WalletBase):
    user_wallet: int
