# -*- coding: utf-8 -*- 
 
# 用pandas 读入 国家数据分省数据指标
import pandas as pd
df = pd.DataFrame.from_csv("data/fsnd_national.tsv", encoding='utf8', sep='\t')
df = df.fillna('<i>（缺省值）</i>')   # nan 用  '（缺省值）' 代替
national = df.set_index('ISO').to_dict()
print("指标有",len(national['WEO_Subject_Code']),'个')


 

# Web app  
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_zb_number = len(national['WEO_Subject_Code']),
                           the_list_items = national['WEO_Subject_Code'],
                           the_title='欢迎来到网上查国家GDP！')


@app.route('/pick_a_zb', methods=['POST'])
def pick_a_zb() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入）找出指标说明"""
    user_zb = request.form['user_zb']	
    return render_template('results.html',
                           the_title = '以下是您选取的结果：',
                           the_zb = user_zb,
                           the_zb_WEO_Subject_Code = national['WEO_Subject_Code'][user_zb],
                          
						   
						   
						   
                           )


if __name__ == '__main__':
    app.run(debug=True)