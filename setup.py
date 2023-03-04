from setuptools import setup, find_packages

setup(
    name='pptx2pdf',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pptx2pdf = pptx2pdf.pptx2pdf:main'
        ]
    }
)
