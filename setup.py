#setup.py
#intended for CursedChambers.py

import setuptools
with open("README.txt", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="Anita",
	version="1.0.0",
	author="Anita Whyatt",
	author_email="anita.whyatt@wsu.edu",
	description="A simple top-down shooter produced to demonstrate the pygame module",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/AnitaWcpts224/cursed_chambers',
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Licence :: OSI Approved :: MIT Licence",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

