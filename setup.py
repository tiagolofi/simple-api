from setuptools import setup, find_packages

setup(
    name="simple-api",
    version="0.0.1",
    description="Um provedor de APIs baseado em arquivos de configuração",
    author="tiagolofi",
    author_email="tiagolofi@example.com",
    url="https://github.com/tiagolofi/simple-api",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "python-dotenv", "pytest", "fastapi", "uvicorn", "python-jose", "passlib[bcrypt]", "PyYAML", "datetime"
    ],
    extras_require={
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
