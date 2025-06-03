# method_resolution_order/payment_processing.py
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class Crypto(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"

class HybridPayment(CreditCard, PayPal, Crypto):
    def process_payment(self, amount):
        # Try CreditCard first, then PayPal, then Crypto
        for method in [CreditCard, PayPal, Crypto]:
            try:
                return super(method, self).process_payment(amount)
            except:
                continue
        raise Exception("No payment method available")

# MRO demonstration
print(HybridPayment.__mro__)
# Output: (<class '__main__.HybridPayment'>, <class '__main__.CreditCard'>, 
#          <class '__main__.PayPal'>, <class '__main__.Crypto'>, 
#          <class '__main__.PaymentMethod'>, <class 'object'>)

payment = HybridPayment()
print(payment.process_payment(100))  # Uses CreditCard's implementation