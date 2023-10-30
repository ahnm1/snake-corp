# Packaging "Native Namespace Packages"  

1. `pip --version`: 21.3 or higher.  
2. `setuptools` version 64 or higher.  

## [Implicit Namespace Packages](https://peps.python.org/pep-0420/)  

Example of a __Namespace Package__ folder structure:  

- [snake-corp](.) (root folder)
  - [snake-corp-datutil](snake-corp-dateutil)
    - [snake_corp](snake-corp-dateutil/snake_corp)
      - [dateutil.py](snake-corp-dateutil/snake_corp/dateutil.py)
    - [pyproject.toml](snake-corp-dateutil/pyproject.toml)

  - [snake-corp-magic-numbers](snake-corp-magic-numbers)
    - [snake_corp](snake-corp-magic-numbers/snake_corp)
      - [magic.py](snake-corp-magic-numbers/snake_corp/magic.py)  
    - [pyproject.toml](snake-corp-magic-numbers/pyproject.toml)

Install with: `python -m pip install -e snake-corp-dateutil/`

These type of packages are a bit __slower__ to import.  
Read more here:  

- <https://realpython.com/python-namespace-package/>
- <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>
- <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>
- <https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>
- <https://packaging.python.org/en/latest/guides/packaging-namespace-packages/>  
