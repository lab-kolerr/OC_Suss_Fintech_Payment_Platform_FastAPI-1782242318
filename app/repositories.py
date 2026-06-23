from sqlalchemy.orm import Session
from app.models import User, Wallet, Transaction, Ledger, FraudDetection, KYCVerification, PaymentMethod, Merchant, Notification
from app.schemas import UserCreate, WalletCreate, TransactionCreate, KYCVerificationResponse

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        db_user = User(email=user.email, hashed_password=user.password)  # Hash password here
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id, User.isDeleted == False).first()

class WalletRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_wallet(self, wallet: WalletCreate) -> Wallet:
        db_wallet = Wallet(user_id=wallet.user_id, balance=wallet.balance)
        self.db.add(db_wallet)
        self.db.commit()
        self.db.refresh(db_wallet)
        return db_wallet

    def get_wallet(self, wallet_id: int) -> Wallet:
        return self.db.query(Wallet).filter(Wallet.id == wallet_id, Wallet.isDeleted == False).first()

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_transaction(self, transaction: TransactionCreate) -> Transaction:
        db_transaction = Transaction(wallet_id=transaction.wallet_id, amount=transaction.amount)
        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        return db_transaction

    def get_transaction(self, transaction_id: int) -> Transaction:
        return self.db.query(Transaction).filter(Transaction.id == transaction_id, Transaction.isDeleted == False).first()

class KYCVerificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_verification(self, user_id: int) -> KYCVerification:
        db_verification = KYCVerification(user_id=user_id)
        self.db.add(db_verification)
        self.db.commit()
        self.db.refresh(db_verification)
        return db_verification

    def get_verification(self, user_id: int) -> KYCVerification:
        return self.db.query(KYCVerification).filter(KYCVerification.user_id == user_id, KYCVerification.isDeleted == False).first()