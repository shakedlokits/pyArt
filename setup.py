from setuptools import setup, find_packages

setup(
    name         = 'wikiart_webcrawler',
    version      = '0.1dev',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = wikiart_webcrawler.settings']},
    install_requires = [
        "Scrapy==1.0.4",
        "scikit-image==0.11.3",
		"scikit-learn==0.17",
		"scipy==0.16.1",
		"numpy==1.10.4",
		"Pillow==3.1.0",
		"boto3==1.2.3",
        "botocore==1.3.22",
    ],
)
