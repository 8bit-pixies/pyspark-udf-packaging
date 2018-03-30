Feature Extensions
==================

`Feature Extensions` are the generic approaches for defining reuseable code modules/blocks which can be orchestrated with the `Feature Compute` engine. Extensions typically are documented and demonstrates how to use it. 

Extensions should also be seperated by `entity` type and imported via the pattern

```py
import feature_foo
```

Building Extensions
===================

Please consider reading XXX to develop your own features. 

Installing
==========

For development.

```sh
pip install . --force-reinstall --upgrade --ignore-installed
```

or from git, to install the latest version on master:

```sh
pip install git+ssh://git@bitbucket:2222/feat/feature.generic.git@master#"egg=feature_generic&subdirectory=python" --upgrade --ignore-installed
```

For production please use:

```sh
pip install feature-generic --index-url http://pypi.int.corp.sun/cdto/release --trusted-host pypi.int.corp.sun
```

Running Tests
=============

In root directory simply run:

```py
nosetests
```

Upgrading to prod
=================

```
# registration
python setup.py register -r cdtorelease

# upload
python setup.py sdist upload -r cdtorelease
```