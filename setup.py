from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="send_simple_email",
    version="0.0.1",
    author="William Onate",
    author_email="contatowilliamrco@gmail.com",
    description="Send Simple E-mails with Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OnateWill/send_email_py/blob/main/send_simple_email/enviar_email_com_python.py",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10')