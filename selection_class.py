class DocumentSelectionMetadata:
    def __init__(self,title_entry, filename_entry, publisher_options, structure_options, document_options):
        self.title = title_entry
        self.filename = filename_entry
        self.publisher = publisher_options
        self.structure_type = structure_options
        self.document_type = document_options
    