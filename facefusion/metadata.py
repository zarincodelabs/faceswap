METADATA =\
{
	'name': '<a href="https://anas.zarin.solutions" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="500" data-original-width="500" height="200" src="https://photos.zarin.solutions/logos/anas/web.png" width="200" /></a>',
	'description': 'Next generation face swapper and enhancer',
	'version': '3.0',
	'license': 'MIT',
	'author': 'Anas Muhammad',
	'url': 'https://anas.zarin.solutions'
}


def get(key : str) -> str:
	return METADATA[key]
