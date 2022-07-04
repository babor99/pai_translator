from selenium import webdriver
from selenium.webdriver.common.by import By

from fpdf import FPDF

import time

def translateDataAndMakePDF(json_data, out_filename):
    text = json_data['text']
    lang_list = json_data['languages']
    if not out_filename:
        out_filename = 'Default.pdf'
    print('lang_list: ', lang_list)
    print('outout_filename: ',out_filename)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(chrome_options=options)

    driver = webdriver.Chrome(chrome_options=options)
    lang_codes = {'Bangla': 'bn', 'Hindi': 'hi', 'Chinese': 'zh-CN', 'Japanese': 'ja'}
    for lang in lang_list:
        output_text = ""
        ln_code = lang_codes[lang]
        driver.get(f"https://translate.google.com/?sl=auto&tl={ln_code}&text={text}&op=translate")
        time.sleep(5)

        output = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]').text
        output_text += f"\n\n{lang}\n\n"
        output_text += output
        print('language: ', lang)
        print("Translated Paragraph:=> " + output)

        with open(f'{lang}.txt', 'w+', encoding='utf-8') as file:
            file.write(output_text)

    pdf = FPDF()      
    pdf.add_page() 

    for lang in lang_list:

        if lang == 'Bangla':
            pdf.add_font('Roman Unicode', '', 'roman-unicode-regular.ttf', uni=True)
            pdf.set_font("Roman Unicode", size = 12)
            with open(f'{lang}.txt', 'r', encoding='utf-8') as f:
                print('file: ', f)
                for x in f:
                    print('x: ', x)
                    pdf.cell(50, 5, txt = x, ln = 1, align = 'L')
        if lang == 'Hindi':
            pdf.add_font('Hind', '', 'Hind-Light.ttf', uni=True)
            pdf.set_font("Hind", size = 12)
            with open(f'{lang}.txt', 'r', encoding='utf-8') as f:
                print('file: ', f)
                for x in f:
                    print('x: ', x)
                    pdf.cell(50, 5, txt = x, ln = 1, align = 'L')
        if lang == 'Chinese':
            pdf.add_font('XiaolaiSC-Regular', '', 'XiaolaiSC-Regular.ttf', uni=True)
            pdf.set_font("XiaolaiSC-Regular", size = 12)
            with open(f'{lang}.txt', 'r', encoding='utf-8') as f:
                print('file: ', f)
                for x in f:
                    print('x: ', x)
                    pdf.cell(50, 5, txt = x, ln = 1, align = 'L')
        if lang == 'Japanese':
            pdf.add_font('Naikai Font', '', 'Kosefont-JP.ttf', uni=True)
            pdf.set_font("Naikai Font", size = 12)
            with open(f'{lang}.txt', 'r', encoding='utf-8') as f:
                print('file: ', f)
                for x in f:
                    print('x: ', x)
                    pdf.cell(50, 5, txt = x, ln = 1, align = 'L')
        
    if out_filename.endswith('.pdf'):
        pdf.output(out_filename)
    else:
        pdf.output(f"{out_filename}.pdf")


    driver.close()




