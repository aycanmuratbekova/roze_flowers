import crypt
import hashlib
from collections import OrderedDict

from main.settings import MERCHANT_ID, SECRET, SIGNATURE


def get_sig(param):
    sig = SIGNATURE
    ordered_dict = OrderedDict(sorted(param.items()))
    for key, value in ordered_dict.items():
        sig += ';' + str(value)
    sig += ';' + SECRET
    hashed_sig = hashlib.md5(sig.encode()).hexdigest()
    return hashed_sig


def get_salt():
    return crypt.mksalt(crypt.METHOD_SHA512)


def get_params(payment):

    params = dict(
        pg_order_id=payment.id,
        pg_merchant_id=MERCHANT_ID,
        pg_amount=payment.amount,
        pg_description=payment.description,
        pg_salt=get_salt(),
        pg_success_url=f"http://127.0.0.1:8000/payments/transaction/success/",
        pg_failure_url='http://127.0.0.1:8000/payments/transaction/failure/',
    )
    return params


def is_real_signature(request):
    if request:
        return True
    return False



