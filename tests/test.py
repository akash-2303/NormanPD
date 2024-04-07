from assignment2.newmain import get_pdf_reader, lines_from_pages, dataframe_from_lines

# Sample data for testing
file_path = "C:/Users/Akash Balaji/Downloads/DATA ENGINEERING/cis6930sp24-assignment2/2024-02-01_daily_incident_summary.pdf"

sample_pdf_path = file_path
sample_lines = [['02/01/2024 00:10', '2024-00012345', '123 MAIN ST', 'Traffic Stop', 'PD123'],
                ['02/01/2024 00:15', '2024-00012346', '456 ELM ST', 'Suspicious Activity', 'PD456']]

def test_get_pdf_reader():
    pdf_reader = get_pdf_reader(sample_pdf_path)
    assert pdf_reader is not None

def test_lines_from_pages():
    pdf_reader = get_pdf_reader(sample_pdf_path)
    lines = lines_from_pages(pdf_reader)
    assert len(lines) > 0

def test_dataframe_from_lines():
    df = dataframe_from_lines(sample_lines)
    assert len(df) == 2
    assert list(df.columns) == ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
