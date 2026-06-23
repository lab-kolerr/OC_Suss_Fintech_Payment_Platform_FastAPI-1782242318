from fastapi import APIRouter
from .models import User, Wallet, Transaction, Ledger, FraudDetection, KYCVerification, PaymentMethod, Merchant, Notification

router = APIRouter()

@router.get("/users/")
async def get_users():
    return []

@router.post("/users/")
async def create_user(user: User):
    return user

@router.get("/wallets/")
async def get_wallets():
    return []

@router.post("/wallets/")
async def create_wallet(wallet: Wallet):
    return wallet

@router.get("/transactions/")
async def get_transactions():
    return []

@router.post("/transactions/")
async def create_transaction(transaction: Transaction):
    return transaction

@router.get("/ledgers/")
async def get_ledgers():
    return []

@router.post("/ledgers/")
async def create_ledger(ledger: Ledger):
    return ledger

@router.get("/fraud-detection/")
async def get_fraud_detections():
    return []

@router.post("/fraud-detection/")
async def create_fraud_detection(fraud_detection: FraudDetection):
    return fraud_detection

@router.get("/kyc-verification/")
async def get_kyc_verifications():
    return []

@router.post("/kyc-verification/")
async def create_kyc_verification(kyc_verification: KYCVerification):
    return kyc_verification

@router.get("/payment-methods/")
async def get_payment_methods():
    return []

@router.post("/payment-methods/")
async def create_payment_method(payment_method: PaymentMethod):
    return payment_method

@router.get("/merchants/")
async def get_merchants():
    return []

@router.post("/merchants/")
async def create_merchant(merchant: Merchant):
    return merchant

@router.get("/notifications/")
async def get_notifications():
    return []

@router.post("/notifications/")
async def create_notification(notification: Notification):
    return notification