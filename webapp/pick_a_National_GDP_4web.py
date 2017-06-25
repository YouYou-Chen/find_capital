# -*- coding: utf-8 -*- 
# 使用模块module national
import national  
c = national.national_list_name()
c_list = [c.data[k] for k in sorted(c.data.keys())]
c_dict_reverse = {v:k for k, v in c.data.items()}



from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_list_items = c_list ,
						   the_title='欢迎来到网上查找世界各个国家的GDP情况！')


@app.route('/pick_a_National_GDP', methods=['POST'])
def pick_a_color() -> 'html':
	user_national_ISO= request.form['user_ISO']
	user_national_WEO_Subject_Code= request.form['user_WEO_Subject_Code']
	with open('WEOApr2017all.tsv', 'r', encoding='utf8') as national_data:
		line = national_data.readlines()
	want_ISO=[i for i in line if user_national_ISO in i]
	want_WEO=[i for i in want_ISO if user_national_WEO_Subject_Code in i]
	want_nation=[i for i in want_WEO if user_national_user_nation in i]
	result_nation=[]
	for i in range(len(set(want_nation))):
		u=str(i+1)
		a=want_nation[i].split('\t')[10]
		b=want_nation[i].split('\t')[11]
		c=want_nation[i].split('\t')[12]
		d=want_nation[i].split('\t')[13]
		e=want_nation[i].split('\t')[14]
		f=want_nation[i].split('\t')[15]
		h=want_nation[i].split('\t')[16]
		i=want_nation[i].split('\t')[17]
		j=want_nation[i].split('\t')[18]
		k=want_nation[i].split('\t')[19]
		l=want_nation[i].split('\t')[20]
		m=want_nation[i].split('\t')[21]
		n=want_nation[i].split('\t')[22]
		o=want_nation[i].split('\t')[23]
		p=want_nation[i].split('\t')[24]
		q=want_nation[i].split('\t')[25]
		r=want_nation[i].split('\t')[26]
		s=want_nation[i].split('\t')[27]
		t=want_nation[i].split('\t')[28]
		u=want_nation[i].split('\t')[29]
		v=want_nation[i].split('\t')[30]
		w=want_nation[i].split('\t')[31]
		x=want_nation[i].split('\t')[32]
		y=want_nation[i].split('\t')[33]
		z=want_nation[i].split('\t')[34]
		A=want_nation[i].split('\t')[35]
		B=want_nation[i].split('\t')[36]
		C=want_nation[i].split('\t')[37]
		D=want_nation[i].split('\t')[38]
		E=want_nation[i].split('\t')[39]
		F=want_nation[i].split('\t')[40]
		G=want_nation[i].split('\t')[41]
		H=want_nation[i].split('\t')[42]
		I=want_nation[i].split('\t')[43]
		J=want_nation[i].split('\t')[44]
		K=want_nation[i].split('\t')[45]
		L=want_nation[i].split('\t')[46]
		M=want_nation[i].split('\t')[47]
		N=want_nation[i].split('\t')[48]
		O=want_nation[i].split('\t')[49]
		P=want_nation[i].split('\t')[50]
				
		
		
		result_nation=sorted(result_nation)
		
		
	return render_template('results.html',
							the_title = '以下是您筛选后的结果：',
							the_national_code= result_nation,
							the_national_ISO_code =user_national_ISO,
							the_national_WEO_Subject_Code_code =user_national_WEO_Subject_Code,
					
							)

if __name__ == '__main__':
    app.run(debug=True)
