from __future__ import annotations
from typing import TypeVar, Generic, Optional
from node import Node, Loan


T = TypeVar("T")


class LoanLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    def append(self, data: T):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def find_loan(self, loan_id: str) -> Optional[T]:
        current = self.head
        while current:
            if current.data.loan_id == loan_id:
                return current.data
            current = current.next
        return None

    def update_status(self, loan_id: str, new_status: str, approved_amount: float = None):
        loan = self.find_loan(loan_id)
        if loan:
            loan.status = new_status
            if approved_amount is not None:
                loan.approved_amount = approved_amount
                loan.generate_payment_plan()


# Function to create a new loan application
def create_loan_application(loan_list: LoanLinkedList[Loan]):
    associate_id = input("Ingrese el número de asociado: ")
    amount_requested = float(input("Monto solicitado: "))
    num_installments = int(input("Número de cuotas: "))
    monthly_income = float(input("Ingresos mensuales: "))
    guarantee = input("Garantía que deja el asociado: ")
    loan = Loan(associate_id, amount_requested, num_installments, monthly_income, guarantee)
    loan_list.append(loan)
    print(f"Prestamo creado con ID: {loan.loan_id}")


# Function to approve a loan
def approve_loan(loan_list: LoanLinkedList[Loan]):
    loan_id = input("Ingrese el ID del préstamo a aprobar: ")
    approved_amount = float(input("Ingrese el monto aprobado: "))
    loan_list.update_status(loan_id, "approved", approved_amount)
    print(f"Préstamo {loan_id} aprobado con monto {approved_amount}")


# Function to make a payment
def make_payment(loan_list: LoanLinkedList[Loan]):
    loan_id = input("Ingrese el ID del préstamo para realizar un pago: ")
    payment_amount = float(input("Ingrese el monto del pago: "))
    loan = loan_list.find_loan(loan_id)
    if loan:
        loan.make_payment(payment_amount)
        print(f"Pago de {payment_amount} realizado al préstamo {loan_id}")
    else:
        print("Préstamo no encontrado.")