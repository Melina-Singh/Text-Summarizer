import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Melina-Singh"
SRC_REPO = "textSummarizer"  # Changed variable name to lowercase
AUTHOR_EMAIL = "melinacingh@gmail.com"

setuptools.setup(
    name=SRC_REPO,  # Changed to lowercase variable
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    long_description=long_description,  # Corrected to lowercase
    long_description_content_type="text/markdown",  # Corrected to lowercase
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={'': 'src'},  # Fixed the mapping of package_dir
    packages=setuptools.find_packages(where="src"),  # Ensure the packages are in the 'src' folder
)
