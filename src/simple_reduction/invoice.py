import fitz
import logging

logger = logging.getLogger(__name__)

class Invoice:
    """
    A class used to represent an Invoice.

    Attributes
    ----------
    doc : fitz.fitz.Document
        a PyMuPDF Document object representing the PDF invoice
    invoice_type : str
        a string that represents the type of the invoice
    """

    def __init__(self, doc):
        """
        Construct a new 'Invoice' object.

        Parameters
        ----------
        doc : fitz.fitz.Document
            a PyMuPDF Document object representing the PDF invoice
        """

        self.doc = doc
        self.invoice_type = None

    def classify_invoice(self, invoice_identifiers):
        """
        Classify the invoice by searching for unique identifiers in the text.

        Parameters
        ----------
        invoice_identifiers : dict
            a dictionary mapping invoice types to unique identifiers
        """

        for variant, identifier in invoice_identifiers.items():
            for page in self.doc:
                instances = page.search(identifier)
                if instances:
                    self.invoice_type = variant
                    return

    def redact_invoice(self, redaction_areas):
        """
        Redact certain areas of the invoice.

        Parameters
        ----------
        redaction_areas : dict
            a dictionary mapping invoice types to lists of areas to redact
        """

        if not self.invoice_type:
            logger.error("Invoice type not determined. Cannot redact.")
            return

        for area in redaction_areas[self.invoice_type]:
            for page in self.doc:
                page.addRedactAnnot(area["coordinates"])
        self.doc.apply_redactions()

    def save(self, output_file):
        """
        Save the redacted invoice to a PDF file.

        Parameters
        ----------
        output_file : str
            path where the redacted PDF file will be saved
        """

        self.doc.save(output_file, garbage=4, deflate=True, clean=True)
