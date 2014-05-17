# -*- coding: utf-8 -*-

from __future__ import unicode_literals

__all__ = [
    "__packagename__",
    "__version__",
    "__summary__",
    "__url__",
    "__author__",
    "__email__",
    "__license__"
]

# The name of the package 
__packagename__ = "{{cookiecutter.repo_name}}"

# A version number like 3.1.4 or 1.0a3 
__version__ = "{{cookiecutter.version}}"

# A one-line summary of what the package does. It's like the first line of a doc string. 
__summary__ = "{{cookiecutter.project_short_description}}"

# The URL of the package's home page 
__url__ = "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}"

# The name of the author 
__author__ = "{{cookiecutter.full_name}}"

# The email address of the author. (PEP 241 mentions that this might be used as a unique key in some catalog of packages, but I don't know if it actually is.) 
__email__ = "{{cookiecutter.email}}"

# PEP 241 says to put the name of the license here, but I don't think that's a good idea. The name doesn't identify a specific license. There are several Zope licenses and several PSF licenses. I recommend putting the URL of the license. 
__license__ = "{{cookiecutter.license_name}}"
