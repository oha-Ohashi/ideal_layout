f_names = [
	{
		'before': 'en_long.txt',
		'after': 'en.txt'
	},
	{
		'before': 'ja_long.txt',
		'after': 'ja.txt'
	}
]

n_chars = 1000

for f_name in f_names:
	with open(f_name['before'], 'r') as f:
		text = f.read()
		print(len(text)) 
		text = text[0:n_chars]
	with open(f_name['after'], 'w') as f:
		print(len(text)) 
		f.write(text)