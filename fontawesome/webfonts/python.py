import requests

version=["5.0.0","5.0.1","5.0.3","5.0.5","5.0.7","5.0.9","5.0.10","5.0.11","5.0.13","5.1.0","5.1.1","5.2.0","5.3.0","5.4.0","5.4.1","5.5.0","5.6.0","5.6.1","5.6.3","5.7.0","5.7.1","5.8.0","5.8.2","5.9.0","5.10.1","5.10.2","5.11.0","5.11.1","5.11.2","5.12.0","5.12.1","5.13.0","5.13.1"]

ext=["woff","woff2","eot","ttf"]

brands=["solid-900","regular-400","light-300","duotone-900","brands-400"]
for x in version:
	for y in ext:
		for z in brands:
			url='https://kit-pro.fontawesome.com/releases/latest/webfonts/pro-fa-'+z+'-'+x+'.'+y
			r = requests.get(url,allow_redirects=True)
			open('pro-fa-'+z+'-'+x+'.'+y,'wb').write(r.content)

