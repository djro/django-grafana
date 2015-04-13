from setuptools import setup, find_packages

LONG_DESC = """
TODO
"""

setup(
    name='django-grafana',
    packages=find_packages(),
    version='0.0.1',
    long_description=LONG_DESC,
    description='Django backend for Grafana.',
    author='Alex Gavrisco',
    author_email='alexandr@gavrisco.com',
    url='https://github.com/Alexx-G/django-grafana',
    download_url='https://github.com/Alexx-G/django-grafana',
    keywords=['grafana', 'backend', 'telementry', 'metrics', 'django', 'python'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        ],
    install_requires=[
        "Django>=1.7",
        "djangorestframework>=3.0",
    ]
    )