from distutils.core import setup
setup(
  name = 'PyDif',         
  packages = ['PyDif'],   
  version = '2.0',      
  license='MIT',        
  description = 'PyDif Duplicate Image Finder - searches for duplicate image files within a specified folder path.', 
  author = 'Elise Landman',                  
  author_email = 'elisejlandman@hotmail.com', 
  url = 'https://github.com/elisemercury/Duplicate-Image-Finder', 
  download_url = 'https://github.com/elisemercury/Duplicate-Image-Finder/archive/refs/tags/v2.0.tar.gz',    # change everytime for each new release
  keywords = ['duplicate', 'image', 'finder', "similarity", "pictures"],  
  install_requires=[          
          'scikit-image',
          'matplotlib',
          'numpy',
          'opencv-python',
          'imghdr',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which pyhton versions to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)