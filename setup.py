import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='mooc_anon',
     version='0.1',
     scripts=['mooc_anon.py'] ,
     author="Emmanuel Acheampong",
     author_email="achampion.emma@gmail.com",
     description="MOOC Anonymous is a python package for helping the online learning community.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/acheamponge/mooc_anon",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
