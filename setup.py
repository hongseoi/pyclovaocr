import setuptools

setuptools.setup(
    name="pyclovaocr",
    version="1.0",
    license='MIT',
    author="kdr",
    author_email="kdrhacker1234@gmail.com",
    description="Unofficial Clova AI OCR python wrapper",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kdrkdrkdr/pyclovaocr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['requests'],
    py_modules = ['pyclovaocr']
)