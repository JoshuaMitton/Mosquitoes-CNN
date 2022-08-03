from setuptools import setup
from setuptools import find_packages

setup(name='Mosquitoes Project Josh Mitton Thesis',
      version='1.0',
      description='Mosquitoes Project Josh Mitton Thesis',
      author='Josh Mitton',
      author_email='j.mitton.1@research.gla.ac.uk',
      url='https://joshuamitton.github.io',
      download_url='https://github.com/JoshuaMitton/Mosquitoes-CNN',
      license='GNU GENERAL PUBLIC LICENSE',
      install_requires=['numpy>=1.17.2',
                        'tensorflow>=1.12.0',
                        'keras>=2.2.4',
                        'tqdm>=4.36.1',
                        'pandas>=0.25.1',
                        'matplotlib>=3.1.1',
                        'sklearn>=0.24.2',
                        'umap-learn>=0.5.3',
                        'h5py>=2.10.0',
                        'scipy>=1.6.0'],
      package_data={'Mosquitoes-CNN': ['README.md']},
      packages=find_packages())
