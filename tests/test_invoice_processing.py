import os
import fitz
import pytest
from simple_reduction.invoice import Invoice
from simple_reduction.invoice_redaction import main
from tests import root_folder

@pytest.fixture(scope="module")
def xtest_data_dir():
    # Path to the test data directory
    return root_folder / "data/test-data"

@pytest.fixture(scope="module")
def output_pdf_dir():
    # Path to the directory to store the output redacted PDFs
    output_dir = root_folder / "data/test-data/output"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def test_classification(xtest_data_dir):
    # Iterate over the items in the test data directory
    for filename in os.listdir(xtest_data_dir):
        item_path = os.path.join(xtest_data_dir, filename)

        # Load the invoice PDF
        doc = fitz.open(item_path)
        invoice = Invoice(doc)

        # Extract the expected invoice type from the filename
        expected_invoice_type = filename.split(".")[0]

        # Classify the invoice
        invoice.classify_invoice()

        # Verify the invoice type
        assert invoice.invoice_type == expected_invoice_type

def test_reduction(xtest_data_dir, output_pdf_dir):
    # Iterate over the items in the test data directory
    for filename in os.listdir(xtest_data_dir):
        item_path = os.path.join(xtest_data_dir, filename)

        if os.path.isdir(item_path):
            continue

        invoice_path = item_path
        output_pdf_path = os.path.join(output_pdf_dir, filename)

        # Run the main function with the invoice and output PDF paths
        main(invoice_path, output_pdf_path)

        # Check if the output PDF file was created
        assert os.path.exists(output_pdf_path)

        # Load the output redacted PDF
        doc = fitz.open(output_pdf_path)
        invoice = Invoice(doc)

        # Verify that the redaction annotations were added to the invoice
        assert len(invoice.page.annots) > 0
