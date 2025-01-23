# ex1.py

from decimal import Decimal

class Account:
    """
    Account class for maintaining a bank account balance.
    """

    def __init__(self, name: str, balance: Decimal):
        """
        Initialize an Account object.

        Args:
            name (str): The account holder's name.
            balance (Decimal): The initial account balance.

        Raises:
            ValueError: If the initial balance is less than 0.00.
        """
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
        self._name = name
        self._balance = balance

    @property
    def name(self) -> str:
        """
        Get the account holder's name.

        Returns:
            str: The account holder's name.
        """
        return self._name

    @property
    def balance(self) -> Decimal:
        """
        Get the current account balance.

        Returns:
            Decimal: The current account balance.
        """
        return self._balance

    @balance.setter
    def balance(self, value: Decimal) -> None:
        """
        Set the account balance.

        Args:
            value (Decimal): The new account balance.

        Raises:
            ValueError: If the new balance is less than 0.00.
        """
        if value < Decimal('0.00'):
            raise ValueError('Balance must be >= to 0.00.')
        self._balance = value

    def deposit(self, amount: Decimal) -> None:
        """
        Deposit money to the account.

        Args:
            amount (Decimal): The amount to deposit.

        Raises:
            ValueError: If the amount is less than 0.00.
        """
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        """
        Withdraw money from the account.

        Args:
            amount (Decimal): The amount to withdraw.

        Raises:
            ValueError: If the amount is greater than the balance or less than 0.00.
        """
        if amount > self.balance:
            raise ValueError('Amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance -= amount
