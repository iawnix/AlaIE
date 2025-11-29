from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

setup(
      name="AlaIE"
    , version="1.0"
    , author="iawnix"
    , author_email="iawnix@163.com"
    , description="Based on the work of John Z. H. Zhang et al.[DOI: 10.1021/acs.jctc.7b01295], this implementation was carried out."
    , install_requires=read_requirements()
    , packages=find_packages()
    , entry_points={
        "console_scripts": [
            "AlaIE=src.run:main"]}
    , python_requires=">=3.10"
)
