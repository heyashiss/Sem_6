from decimal import Decimal

class Invoice:
    def __init__(self, part_number: str, part_description: str, quantity: int, price: Decimal):
        self._part_number = part_number
        self._part_description = part_description
        self.quantity = quantity
        self.price = price

    @property
    def part_number(self) -> str:
        return self._part_number

    @property
    def part_description(self) -> str:
        return self._part_description

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError('Quantity must be non-negative.')
        self._quantity = value

    @property
    def price(self) -> Decimal:
        return self._price

    @price.setter
    def price(self, value: Decimal) -> None:
        if value < Decimal('0.00'):
            raise ValueError('Price must be non-negative.')
        self._price = value

    def calculate_invoice(self) -> Decimal:
        return self.quantity * self.price

    def __repr__(self):
        return (f'Invoice(part_number={self.part_number}, part_description={self.part_description}, quantity={self.quantity}, price={self.price})')

    def __str__(self):
        return f'Part Number: {self.part_number}\nPart Description: {self.part_description}\nQuantity: {self.quantity}\nPrice: {self.price}\nInvoice Amount: {self.calculate_invoice()}'


invoice = Invoice('12345', 'Hammer', 2, Decimal('19.99'))
print(invoice)

invoice.quantity = 3
invoice.price = Decimal('20.99')
print(invoice)
