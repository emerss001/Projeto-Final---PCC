function HTMLtoPDF(){
    var element = document.getElementById('Recibo');
    html2pdf(element, {
            margin:       1,
            filename:     'myfile.pdf',
            html2canvas:  { scale: 1, logging: true, dpi: 192, letteRendering: true },
            jsPDF:        { unit: 'cm', format: 'a4', orientation: 'portrait' }
    });
    
}


// Default export is a4 paper, portrait, using millimeters for units
