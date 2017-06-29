# -*- coding: utf-8 -*- 
 
# 用pandas 读入 国家数据分省数据指标
import pandas as pd
df = pd.DataFrame.from_csv("data/fsnd_national.tsv", encoding='utf8', sep='\t')
df = df.fillna('<i>（缺省值）</i>')   # nan 用  '（缺省值）' 代替
national = df.set_index('ISO2_or_country_name').to_dict()
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
                           the_zb_Scale  = national['Scale'][user_zb],
						   the_zb_1980   = national['1980'][user_zb],
                           the_zb_1981   = national['1981'][user_zb],
                           the_zb_1982   = national['1982'][user_zb],
						   the_zb_1983   = national['1983'][user_zb],
						   the_zb_1984   = national['1984'][user_zb],
						   the_zb_1985   = national['1985'][user_zb],
						   the_zb_1986   = national['1986'][user_zb],
						   the_zb_1987   = national['1987'][user_zb],
						   the_zb_1988   = national['1988'][user_zb],
						   the_zb_1989   = national['1989'][user_zb],
						   the_zb_1990   = national['1990'][user_zb],
						   the_zb_1991   = national['1991'][user_zb],
						   the_zb_1992   = national['1992'][user_zb],
						   the_zb_1993   = national['1993'][user_zb],
						   the_zb_1994   = national['1994'][user_zb],
						   the_zb_1995   = national['1995'][user_zb],
						   the_zb_1996   = national['1996'][user_zb],
						   the_zb_1997   = national['1997'][user_zb],
						   the_zb_1998   = national['1998'][user_zb],
						   the_zb_1999   = national['1999'][user_zb],
						   the_zb_2000   = national['2000'][user_zb],
						   the_zb_2001   = national['2001'][user_zb],
						   the_zb_2002   = national['2002'][user_zb],
						   the_zb_2003   = national['2003'][user_zb],
						   the_zb_2004   = national['2004'][user_zb],
						   the_zb_2005   = national['2005'][user_zb],
						   the_zb_2006   = national['2006'][user_zb],
						   the_zb_2007   = national['2007'][user_zb],
						   the_zb_2008   = national['2008'][user_zb],
						   the_zb_2009   = national['2009'][user_zb],
						   the_zb_2010   = national['2010'][user_zb],
						   the_zb_2011   = national['2011'][user_zb],
						   the_zb_2012   = national['2012'][user_zb],
						   the_zb_2013   = national['2013'][user_zb],
						   the_zb_2014   = national['2014'][user_zb],
						   the_zb_2015   = national['2015'][user_zb],
						   the_zb_2016   = national['2016'][user_zb],
						   the_zb_2017   = national['2017'][user_zb],
						   the_zb_2018   = national['2018'][user_zb],
						   the_zb_2019   = national['2019'][user_zb],
						   the_zb_2020   = national['2020'][user_zb],
						   the_zb_2021   = national['2021'][user_zb],
						   the_zb_2022   = national['2022'][user_zb]
						   
						   
						   
						   
                           )


if __name__ == '__main__':
    app.run(debug=True)