from __future__ import annotations
from typing import TypeVar, Generic, List, Optional
from itertools import count

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next_node: Optional[Node[T]] = None):
        self.data = data
        self.next = next_node


class Loan:
    _id_counter = count(1)

    def __init__(self, associate_id: str, amount_requested: float, num_installments: int, monthly_income: float, guarantee: str, attachments: List[str] = None):
        self.loan_id = f"L{next(Loan._id_counter):03d}"
        self.associate_id = associate_id
        self.status = "created"
        self.amount_requested = amount_requested
        self.num_installments = num_installments
        self.approved_amount = 0.0
        self.monthly_income = monthly_income
        self.guarantee = guarantee
        self.attachments = attachments if attachments is not None else []
        self.payment_plan = []
        self.payment_history = []

    def generate_payment_plan(self):
        if self.approved_amount > 0 and self.num_installments > 0:
            monthly_payment = self.approved_amount / self.num_installments
            self.payment_plan = [monthly_payment for _ in range(self.num_installments)]

    def make_payment(self, payment_amount: float):
        self.payment_history.append(payment_amount)

    def __str__(self):
        return (f"Loan ID: {self.loan_id}, Associate ID: {self.associate_id}, Status: {self.status}, "
                f"Amount Requested: {self.amount_requested}, Number of Installments: {self.num_installments}, "
                f"Approved Amount: {self.approved_amount}, Monthly Income: {self.monthly_income}, "
                f"Guarantee: {self.guarantee}, Payment Plan: {self.payment_plan}, Payment History: {self.payment_history}")
