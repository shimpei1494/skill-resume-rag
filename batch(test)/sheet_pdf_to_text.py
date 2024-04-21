# 使用していないが参考に
import pdfplumber
import os

def save_pdf_text_to_file(pdf_file_path, output_dir):
    # PDFファイルを開く
    with pdfplumber.open(pdf_file_path) as pdf:
        # 全ページを通してテキストを抽出
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'
        
        # 出力ファイルのパスを生成
        output_file_path = os.path.join(output_dir, os.path.basename(pdf_file_path).replace('.pdf', '.txt'))
        
        # テキストをファイルに保存
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(full_text)

# 技術経歴書_宮下裕貴.pdfのテキストを抜き出し、skill_sheetディレクトリに保存
input_file_path = '../skill_sheet/pdf/技術経歴書_名前.pdf'
save_pdf_text_to_file(input_file_path, '../skill_sheet/text')
