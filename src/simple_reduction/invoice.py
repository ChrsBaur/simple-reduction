class Invoice:
    def __init__(self, doc):
        self.doc = doc
        self.page = doc[0]
        self.invoice_type = None

    def classify_invoice(self, invoice_identifiers):
        for variant, identifier in invoice_identifiers.items():
            for instance in self.page.searchFor(identifier):
                self.invoice_type = variant
                return

    def redact_invoice(self, redaction_areas):
        if not self.invoice_type:
            print("Invoice type not determined. Cannot redact.")
            return

        for area in redaction_areas[self.invoice_type]:
            self.page.addRedactAnnot(area)

        self.doc.save(output_file, garbage=4, deflate=True, clean=True)
