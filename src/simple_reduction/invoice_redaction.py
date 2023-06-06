import os
import argparse
import fitz
from .invoice import Invoice

def main(input_file, output_file):
    # Define the unique identifiers for each invoice type
    invoice_identifiers = {
        'Invoice Type 1': 'Unique text 1',
        'Invoice Type 2': 'Unique text 2',
        'Invoice Type 3': 'Unique text 3',
        'Invoice Type 4': 'Unique text 4',
    }

    # Define the redaction areas for each invoice type
    redaction_areas = {
        'Invoice Type 1': [(50, 700, 200, 750), (300, 500, 450, 550)],
        'Invoice Type 2': [(100, 600, 250, 650), (350, 400, 500, 450)],
        'Invoice Type 3': [(150, 500, 300, 550), (400, 300, 550, 350)],
        'Invoice Type 4': [(200, 400, 350, 450), (450, 200, 600, 250)],
    }

    # Open the PDF
    doc = fitz.open(input_file)

    # Create an Invoice object
    invoice = Invoice(doc)

    # Classify the invoice
    invoice.classify_invoice(invoice_identifiers)

    # Redact the invoice
    invoice.redact_invoice(redaction_areas)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Redact sensitive information from invoices')
    parser.add_argument('input_file', type=str, help='The path to the invoice PDF')
    parser.add_argument('output_file', type=str, help='The path to save the redacted PDF')
    args = parser.parse_args()

    main(args.input_file, args.output_file)
