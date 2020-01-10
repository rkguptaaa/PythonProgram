import PyPDF2

class PdfMerger:
    def __init__(self, path, *args):
        self.path = path
        self.filename = args
 
    def pdf_combiner(self):
        merger = PyPDF2.PdfFileMerger()
        for file in self.filename:
            merger.append(file)
            
        merger.write('merged.pdf')
        
        
merger = PdfMerger('./', 'twopage.pdf', 'dummy.pdf')
merger.pdf_combiner()