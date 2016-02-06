from setuptools import setup, find_packages

setup(
    name='33598',
    version='0.2dev',
    packages=['wikiart_webcrawler', 'image_vectorizer'],
    entry_points={'scrapy': ['settings = wikiart_webcrawler.settings']},
    install_requires=[
        "Scrapy==1.0.4",
        "scikit-image==0.11.3",
        "scipy==0.16.1",
        "numpy==1.10.4",
        "Pillow==3.1.0",
    ],
)
