import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='comment_generator',
     version='0.0.1',
     scripts=['./comment_generator/comment_generator.py'] ,
     author="Ivan Ivanov",
     author_email="isivanov98@outlook.com",
     description="A Docker and AWS utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/divakaivan/icc-comments",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )