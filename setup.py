import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='comment_creator',
     version='0.0.4',
     scripts=['./comment_creator/comment_creator.py'] ,
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