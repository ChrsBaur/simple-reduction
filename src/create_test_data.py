from faker import Faker
from fpdf import FPDF
import os
from tests import root_folder


class InvoiceGenerator:
    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address
        self.fake = Faker()

    def generate_invoice_number(self):
        return str(self.fake.random_number(digits=6))

    def generate_invoice_date(self):
        return self.fake.date_between(start_date='-1y', end_date='today')

    def generate_due_date(self, invoice_date):
        return self.fake.date_between(start_date=invoice_date, end_date='+30d')

    def generate_customer_details(self):
        customer_name = self.fake.name()
        customer_address = self.fake.address()
        return customer_name, customer_address

    def generate_invoice_items(self):
        items = []
        for _ in range(2):
            item_name = self.fake.word()
            quantity = self.fake.random_int(min=1, max=10)
            price = self.fake.random_int(min=10, max=100)
            items.append((item_name, quantity, price))
        return items

    def create_invoice(self, pdf_name, invoice_type):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Write invoice type in the header
        pdf.cell(0, 10, txt=invoice_type, ln=True, align='C')
        pdf.ln(10)

        invoice_number = self.generate_invoice_number()
        invoice_date = self.generate_invoice_date()
        due_date = self.generate_due_date(invoice_date)
        customer_name, customer_address = self.generate_customer_details()
        items = self.generate_invoice_items()

        # Determine the layout configuration based on the invoice type
        if invoice_type == "Invoice Type 1":
            # Variant 1 layout
            pdf.cell(0, 10, txt=self.company_name, ln=True, align='L')
            pdf.cell(0, 10, txt=self.company_address, ln=True, align='L')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Invoice Number: " + invoice_number, ln=True, align='L')
            pdf.cell(0, 10, txt="Invoice Date: " + str(invoice_date), ln=True, align='L')
            pdf.cell(0, 10, txt="Due Date: " + str(due_date), ln=True, align='L')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Bill To:", ln=True, align='L')
            pdf.cell(0, 10, txt=customer_name, ln=True, align='L')
            pdf.cell(0, 10, txt=customer_address, ln=True, align='L')
            pdf.ln(10)
            pdf.cell(40, 10, txt="Item", ln=True, align='L')
            pdf.cell(40, 10, txt="Quantity", ln=True, align='C')
            pdf.cell(40, 10, txt="Price", ln=True, align='R')
            pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='L')  # Separator line
            for item in items:
                pdf.cell(40, 10, txt=item[0], ln=True, align='L')
                pdf.cell(40, 10, txt=str(item[1]), ln=True, align='C')
                pdf.cell(40, 10, txt="$" + str(item[2]), ln=True, align='R')
                pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='L')

        elif invoice_type == "Invoice Type 2":
            # Variant 2 layout
            pdf.cell(0, 10, txt=self.company_name, ln=True, align='R')
            pdf.cell(0, 10, txt=self.company_address, ln=True, align='R')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Invoice Number: " + invoice_number, ln=True, align='R')
            pdf.cell(0, 10, txt="Invoice Date: " + str(invoice_date), ln=True, align='R')
            pdf.cell(0, 10, txt="Due Date: " + str(due_date), ln=True, align='R')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Bill To:", ln=True, align='R')
            pdf.cell(0, 10, txt=customer_name, ln=True, align='R')
            pdf.cell(0, 10, txt=customer_address, ln=True, align='R')
            pdf.ln(10)
            pdf.cell(40, 10, txt="Item", ln=True, align='R')
            pdf.cell(40, 10, txt="Quantity", ln=True, align='C')
            pdf.cell(40, 10, txt="Price", ln=True, align='L')
            pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='R')  # Separator line
            for item in items:
                pdf.cell(40, 10, txt=item[0], ln=True, align='R')
                pdf.cell(40, 10, txt=str(item[1]), ln=True, align='C')
                pdf.cell(40, 10, txt="$" + str(item[2]), ln=True, align='L')
                pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='R')

        elif invoice_type == "Invoice Type 3":
            # Variant 3 layout
            pdf.cell(0, 10, txt=self.company_name, ln=True, align='C')
            pdf.cell(0, 10, txt=self.company_address, ln=True, align='C')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Invoice Number: " + invoice_number, ln=True, align='C')
            pdf.cell(0, 10, txt="Invoice Date: " + str(invoice_date), ln=True, align='C')
            pdf.cell(0, 10, txt="Due Date: " + str(due_date), ln=True, align='C')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Bill To:", ln=True, align='C')
            pdf.cell(0, 10, txt=customer_name, ln=True, align='C')
            pdf.cell(0, 10, txt=customer_address, ln=True, align='C')
            pdf.ln(10)
            pdf.cell(40, 10, txt="Item", ln=True, align='C')
            pdf.cell(40, 10, txt="Quantity", ln=True, align='C')
            pdf.cell(40, 10, txt="Price", ln=True, align='C')
            pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='C')  # Separator line
            for item in items:
                pdf.cell(40, 10, txt=item[0], ln=True, align='C')
                pdf.cell(40, 10, txt=str(item[1]), ln=True, align='C')
                pdf.cell(40, 10, txt="$" + str(item[2]), ln=True, align='C')
                pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='C')

        elif invoice_type == "Invoice Type 4":
            # Variant 4 layout
            pdf.cell(0, 10, txt=self.company_name, ln=True, align='L')
            pdf.cell(0, 10, txt=self.company_address, ln=True, align='L')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Invoice Number: " + invoice_number, ln=True, align='L')
            pdf.cell(0, 10, txt="Invoice Date: " + str(invoice_date), ln=True, align='L')
            pdf.cell(0, 10, txt="Due Date: " + str(due_date), ln=True, align='L')
            pdf.ln(10)
            pdf.cell(0, 10, txt="Bill To:", ln=True, align='L')
            pdf.cell(0, 10, txt=customer_name, ln=True, align='L')
            pdf.cell(0, 10, txt=customer_address, ln=True, align='L')
            pdf.ln(10)
            pdf.cell(40, 10, txt="Item", ln=True, align='R')
            pdf.cell(40, 10, txt="Quantity", ln=True, align='C')
            pdf.cell(40, 10, txt="Price", ln=True, align='L')
            pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='L')  # Separator line
            for item in items:
                pdf.cell(40, 10, txt=item[0], ln=True, align='R')
                pdf.cell(40, 10, txt=str(item[1]), ln=True, align='C')
                pdf.cell(40, 10, txt="$" + str(item[2]), ln=True, align='L')
                pdf.cell(0, 10, txt="-----------------------------------------", ln=True, align='L')

        # Save the PDF
        output_dir = root_folder / "data/test-data"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, pdf_name)
        pdf.output(output_path)


if __name__ == "__main__":
    generator = InvoiceGenerator("Your Company Name", "123 Main Street, Anytown, USA")
    generator.create_invoice("invoice_type1.pdf", "Invoice Type 1")
    generator.create_invoice("invoice_type2.pdf", "Invoice Type 2")
    generator.create_invoice("invoice_type3.pdf", "Invoice Type 3")
    generator.create_invoice("invoice_type4.pdf", "Invoice Type 4")
