from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(amount):
        pass
class UPIPayment(PaymentGateway):
    def initiate_payment(self,amount):
        print(f"payment processed using UPI.. with amount:{amount}")
class NetBanking(PaymentGateway):
    def __init__(self,card_number):
        self._card_number=self._mask_card_number(card_number)
    def _mask_card_number(self,card_number):
        return "*****"+card_number[:-4]
    def initiate_payment(self,amount):
        print(f"Processing payment using {self._card_number} with amount:{amount}")