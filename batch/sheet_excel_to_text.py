# 使用していないが参考に
import pandas as pd

def excel_to_markdown(excel_file_path, sheet_name, output_file_path):
    # Excelファイルを読み込む
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    
    # NaN値を空文字列で置き換える
    df.fillna('', inplace=True)
    
    # DataFrameをCSV形式（カンマ区切り）で保存
    df.to_csv(output_file_path, index=False, sep=',', encoding='utf-8')

# 使用例
excel_file_path = '../skill_sheet/Excel/技術経歴書_名前.xlsx'
sheet_name = '経歴書'
output_file_path = '../skill_sheet/md/output.txt'
excel_to_markdown(excel_file_path, sheet_name, output_file_path)